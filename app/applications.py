import streamlit as st
import pandas as pd
from database_main import print_applications

# df = pd.DataFrame(print_applications(True),index=False)
df = print_applications(True)
print(df)
df = pd.DataFrame(df)

df.columns=['id','company', 'role', 'date_applied', 'extracted_skills', 'deadline', 'status', 'notes']
df.drop(columns=['id'],inplace=True)


print(df)

st.title("This is a title")

st.dataframe(
    data = df,
    hide_index=True
)

