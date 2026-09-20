from google import genai
import os
from dotenv import load_dotenv
from job_parser import extract_info
from read_application import get_applications
import streamlit as st, pandas as pd

st.sidebar.header("Job Analytics")

#-----------------------------------
#Api Integration
#-----------------------------------
load_dotenv("api_key.env")
api_key = os.getenv("gemini_api_key")
client = genai.Client(api_key=api_key)

# interaction = client.interactions.create(
#     model="gemini-3.5-flash",
#     input="Which gemini free model is best for fast and accurate results?"
# )

def parse_resume():
    resume_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/database/resume.pdf"
    with os.open(resume_path, 'r') as itr:
        resume_text = itr.read()

    stream = client.interactions.create(
        model = "gemini-3.5-flash",
        input = "Fetch all the necessary tech stack from this resume",
        stream = True
    )

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

    st.header(selected_row['company'] + " Job Insights")
