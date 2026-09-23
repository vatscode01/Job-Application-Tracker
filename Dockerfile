# Stage 1: Build Virtual Environment (VE)
FROM dhi.io/python:3.12 AS builder

WORKDIR /app

# Create VE
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install -r requirements.txt

# copy requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Final Runtime Image
FROM dhi.io/python:3.12

WORKDIR /app

COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

COPY . .

EXPOSE 8000

# CMD ["/venv/bin/python3", "-m", "uvicorn", "activate", "app:app", "--host=0.0.0.0", "--port=8000"]
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["/venv/bin/python3", "-m", "uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]