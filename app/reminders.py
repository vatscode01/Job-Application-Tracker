from read_application import get_applications
import streamlit as st, pandas as pd
from datetime import date

df = get_applications()

applied = pd.to_datetime(df["date_applied"], errors='coerce').dt.date
deadline = pd.to_datetime(df["deadline"], errors='coerce').dt.date
days_left = []

st.header("Reminders")
st.sidebar.header("Get Reminder and Analytics")

today = date.today()
for i in range(0,len(deadline)):
    left = deadline.iloc[i] - today
    days_left.append(
        {
            'id': df['id'].iloc[i],
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
    id = idx['id']
    company = idx['company']
    status = idx['status']
    days = idx['days']

    if(status == "Applied" and int(days)>=7):
        application_follow_up.append([id,company,days])
    elif (status == "Not Applied" and days<7):
        apply_before_deadline.append([id,company,days])
    elif(status == "Interviewed" and days>=7):
        interview_follow_up.append([id,company,days])

st.markdown('Application Follow Up')
st.write(pd.DataFrame(application_follow_up, columns=['Id','Company','Days Remaining']))

st.markdown('Deadline Approaching')
st.write(pd.DataFrame(apply_before_deadline, columns=['Id','Company','Days Remaining']))
# print(apply_before_deadline)

st.markdown('Interview Follow Up')
st.write(pd.DataFrame(interview_follow_up, columns=['Id','Company','Days Remaining']))
