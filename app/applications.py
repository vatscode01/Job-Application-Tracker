import streamlit as st
import pandas as pd
from database_main import print_applications

df = print_applications(True)
df = pd.DataFrame(df)

df.columns=['id','company', 'role', 'date_applied', 'extracted_skills', 'deadline', 'status', 'notes']
df.drop(columns=['id'],inplace=True)

st.title("Job Application Tracker")

with st.form('application_data'):
    company = st.text_input(label = 'Company Name', placeholder='Enter a valid input')
    submitted = st.form_submit_button("Submit",)
    if(submitted):
        st.write(f"Company: {company}")

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

