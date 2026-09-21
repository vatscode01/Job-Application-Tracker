from google import genai
import os
from dotenv import load_dotenv
from job_parser import extract_info
from read_application import get_applications
import streamlit as st

st.sidebar.header("Job Analytics")

#-----------------------------------
#Api Integration
#-----------------------------------
load_dotenv("api_key.env")
api_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=api_key)

def parse_resume(job_description):
    resume_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/database/resume.pdf"
    resume_file = client.files.upload(file = resume_path)
    jd_file = client.files.upload(file = job_description)

    with st.spinner(
      "Analyzing resume and job description with Gemini... Please wait ⏳"
    ):

        response = client.models.generate_content(
            model = "gemini-3.5-flash",
            contents = [
                jd_file,
                resume_file,
                (
                    "Given my resume and a job description. Find all the skillset from this pdf also analyse this from the given job description. Find all the matching skillset with the job description and this resume."
                )
            ],
        )
    st.write(response.text)

#-----------------------------------
# Analytics Dashboard
#-----------------------------------

df = get_applications()

if not df.empty:
    options = df['id'].astype(str) + " - " + df['company'] + " (" + df['role'] + ")"
    selected_option = st.sidebar.selectbox("Select Application to View/Edit Description", options=options.tolist())
    selected_id = int(selected_option.split(" - ")[0])
    selected_row = df[df['id'] == selected_id].iloc[0]
    filename = selected_row['job_description']
    filepath = os.path.join("Job Descriptions", str(filename))

    st.header(selected_row['company'] + "(" + selected_row['role'] + ")" " Job Insights")
    if os.path.exists(filepath):
        parse_resume(filepath)
    else:
        st.write("Upload valid file")

