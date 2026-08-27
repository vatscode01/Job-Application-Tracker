import streamlit as st
import pandas as pd
# from database_main import print_applications
from read_application import get_applications

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
        'deadline':'Deadline'
    }
)

# with st.form('application_data'):
#     company = st.text_input(label = 'Company Name', placeholder='Enter a valid input')
#     submitted = st.form_submit_button("Submit",)
#     if(submitted):
#         st.write(f"Company: {company}")

