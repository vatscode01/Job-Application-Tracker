import streamlit as st, sqlite3
import pandas as pd
from datetime import date

# from database_main import print_applications
from read_application import get_applications
from read_application import insert_application

# df = print_applications(True)
df = get_applications()
df.drop(columns=['id'],inplace=True)

st.title("Job Application Tracker")

# Show Table
st.dataframe(
    data = df,
    hide_index=True,
    column_config={
        'company':'Company Name',
        'role':'Job Role',
        'date_applied':'Date Applied',
        'extracted_skills':'Extracted Skills',
        'deadline':'Deadline',
        'status' : 'Status',
        'notes': 'Notes'
    }
)

with st.form('application_data',clear_on_submit=True):
    company = st.text_input(label = 'Company Name', placeholder='Enter a valid input')
    role = st.text_input(label = 'Job Role', placeholder='Enter a valid input')
    date_applied = st.date_input(label = 'Date Applied',value = "today")
    extracted_skills = st.text_input(label = 'Extracted Skills', placeholder='Enter a valid input')
    deadline = st.date_input(label = 'Application Deadline', value = "today")
    status = st.text_input(label = 'Status', placeholder='Enter a valid input')
    notes = st.text_input(label = 'Notes', placeholder='Enter a valid input')

    submitted = st.form_submit_button("Submit")
    if(submitted):
        # insert_application(company, role, date_applied, extracted_skills, deadline, status, notes)
        df = get_applications()
        conn = sqlite3.connect("database/job_tracker.db")
        # cur = conn.cursor()
        # cur.execute("""
        #     insert into Applications(company, role, date_applied, extracted_skills, deadline, status, notes)
        #     values (?,?,?,?,?,?,?);
        # """,(company, role, date_applied, extracted_skills, deadline, status, notes))
        # conn.commit()
        # conn.close()
        insert_application(company, role, date_applied, extracted_skills, deadline, status, notes)
        st.write("Form Submitted Succesfully")
        # st.write(f"Company: {company}")


