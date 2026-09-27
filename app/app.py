import streamlit as st

import os

base_dir = os.path.dirname(__file__)
frontend_path = os.path.join(base_dir, "frontend.py")
reminders_path = os.path.join(base_dir, "reminders.py")
analytics_path = os.path.join(base_dir, "analytics.py")
ai_analytics_path = os.path.join(base_dir, "ai_analyser.py")

frontend = st.Page(frontend_path, title="Main Page")
reminder = st.Page(reminders_path, title = "Reminders")
analytics = st.Page(analytics_path, title = "Analytics")
ai_analytics = st.Page(ai_analytics_path, title = "AI Job Insights")

pg = st.navigation(
    [frontend, reminder, analytics, ai_analytics]
)

pg.run()