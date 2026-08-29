import streamlit as st

from read_application import get_applications, insert_application
from read_application import delete_application

# df = print_applications(True)
df = get_applications()
# df.drop(columns=['id'],inplace=True)

st.title("**Job Application Tracker**")

# st.link_button(url = "https://localhost:8501/add_application", label = "Exteranl Link")

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
    },
    selection_mode = 'single-row'
)

with st.form('application_data',clear_on_submit=True):
    company = st.text_input(label = 'Company Name', placeholder='Enter a valid input')
    role = st.text_input(label = 'Job Role', placeholder='Enter a valid input')
    date_applied = st.date_input(label = 'Date Applied',value = "today")
    extracted_skills = st.text_input(label = 'Extracted Skills', placeholder='Enter a valid input')
    deadline = st.date_input(label = 'Application Deadline', value = "today")
    status = st.selectbox(label= "Select options", options=['Applied','Not Applied','Interviewed','Selected','Not Selected'])
    notes = st.text_input(label = 'Notes', placeholder='Enter a valid input')

    submitted = st.form_submit_button("Submit")
    if(submitted):
        insert_application(company, role, date_applied, extracted_skills, deadline, status, notes)
        st.success('Form Submitted Succesfully', icon="✅")

