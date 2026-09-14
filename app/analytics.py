from job_parser import extract_info
from read_application import get_applications
import streamlit as st, pandas as pd

st.sidebar.header("Analytics")

company_skillset = extract_info()
df = get_applications()
st.header("Job Analytics")

for idx, arr in company_skillset.items():
    company_row = df[df['id'] == int(idx)]

    if not company_row.empty:
        # .iloc[0] extracts the row as a Series, just like .loc used to do
        company = company_row.iloc[0]['company']
        st.write(pd.DataFrame(data=[company,arr]))
    else:
        print(f"⚠️ ID {idx} not found in the DataFrame.")

