import streamlit as st

frontend_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/frontend.py"
reminders_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/reminders.py"
analytics_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/analytics.py"

frontend = st.Page(frontend_path, title="Main Page")
reminder = st.Page(reminders_path, title = "Reminders")
analytics = st.Page(analytics_path, title = "Analytics")

pg = st.navigation(
    [frontend, reminder, analytics]
)

pg.run()