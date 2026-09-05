from read_application import get_applications
import streamlit as st, pandas as pd
from datetime import date

df = get_applications()

applied = pd.to_datetime(df["date_applied"], errors='coerce').dt.date
deadline = pd.to_datetime(df["deadline"], errors='coerce').dt.date
days_left = []

st.header("Reminders")
st.sidebar.header("Reminder Lega")

today = date.today()
for i in range(0,len(deadline)):
    left = deadline.iloc[i] - today
    days_left.append(
        {
            "company": df['company'].iloc[i],
            "status": df['status'].iloc[i],
            "days": left.days
        }
    )


# ----------------------------------
# Dataframes for reminders
# ----------------------------------

application_follow_up = []
apply_before_deadline = []
interview_follow_up = []

for idx in days_left:

    company = idx['company']
    status = idx['status']
    days = idx['days']

    if(status == "Applied" and int(days)>=7):
        application_follow_up.append({company,days})
    elif (status == "Not Applied" and days<7):
        apply_before_deadline.append({company,days})
    elif(status == "Interviewed" and days>=7):
        interview_follow_up.append({company,days})

# st.write(application_follow_up,apply_before_deadline,interview_follow_up)
st.markdown('Application Follow Up')
st.dataframe(application_follow_up, width = 'stretch')
st.markdown('Deadline Approaching')
st.dataframe(apply_before_deadline, width='stretch')
st.markdown('Interview Follow Up')
st.dataframe(interview_follow_up, width = 'stretch')