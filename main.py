import sqlalchemy as db

print(db.__version__)

db.create_engine(
    "postgresql://postgres:aady_02@localhost:5432/postgres"
)

print(db.select(Applications))