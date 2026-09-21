import streamlit as st

frontend_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/frontend.py"
reminders_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/reminders.py"
analytics_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/analytics.py"
ai_analytics_path = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/app/ai_analyser.py"

frontend = st.Page(frontend_path, title="Main Page")
reminder = st.Page(reminders_path, title = "Reminders")
analytics = st.Page(analytics_path, title = "Analytics")
ai_analytics = st.Page(ai_analytics_path, title = "AI Job Insights")

pg = st.navigation(
    [frontend, reminder, analytics, ai_analytics]
)

pg.run()