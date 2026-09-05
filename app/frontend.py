import streamlit as st, sqlite3, json, pandas as pd

from read_application import get_applications, insert_application

# df = print_applications(True)
df = get_applications()
# df.drop(columns=['id'],inplace=True)


st.title("**Job Application Tracker**")

df["date_applied"] = pd.to_datetime(df["date_applied"], errors='coerce').dt.date
df["deadline"] = pd.to_datetime(df["deadline"], errors='coerce').dt.date

edited_df = st.data_editor(
    data = df,
    hide_index=True,
    column_config={
        'id': 'ID',
        'company': st.column_config.Column("Company", required=True,),
        'status' : st.column_config.SelectboxColumn("Status", options=['Applied','Not Applied','Interviewed','Selected','Not Selected'], default="Applied", required=True),
        'role':'Job Role',
        'date_applied': st.column_config.DateColumn("Date Applied"),
        'extracted_skills':'Extracted Skills',
        'deadline': st.column_config.DateColumn("Deadline"),
        'notes': 'Notes'
    },
    disabled=['id'],
    num_rows = 'dynamic',
    key = 'editor',
)

if(st.button("Submit")):
    edits = st.session_state["editor"]
    
    conn = sqlite3.connect("database/job_tracker.db")
    
    success = False
    try:
        # -------------------------
        # Updated cells
        # -------------------------
        for row_idx, changes in edits["edited_rows"].items():
    
            row_id = int(df.iloc[row_idx]["id"])

            # Only update the columns that actually changed
            for column, new_value in changes.items():

                # Don't allow the primary key to be changed
                if column == "id":
                    continue
                
                if column == "extracted_skills" and isinstance(new_value, str):
                    new_value = json.dumps([s.strip() for s in new_value.split(',') if s.strip()])

                query = f"""
                    UPDATE Applications
                    SET "{column}" = ?
                    WHERE id = ?
                """

                conn.execute(
                    query,
                    (new_value, row_id)
                )

        # -------------------------
        # Deleted rows
        # -------------------------
        for row_idx in edits["deleted_rows"]:

            row_id = int(df.iloc[row_idx]["id"])

            conn.execute(
                "DELETE FROM Applications WHERE id = ?",
                (row_id,)
            )

        # -------------------------
        # Added rows
        # -------------------------
        for row in edits["added_rows"]:
            conn.execute("""
                INSERT INTO Applications(company, role, date_applied, extracted_skills, deadline, status, notes)
                VALUES (?,?,?,?,?,?,?)
            """, (
                row.get('company', ''),
                row.get('role', ''),
                row.get('date_applied', ''),
                json.dumps([s.strip() for s in row.get('extracted_skills', '').split(',') if s.strip()]) if row.get('extracted_skills') else "[]",
                row.get('deadline', ''),
                row.get('status', ''),
                row.get('notes', '')
            ))

        conn.commit()
        st.success("Changes saved successfully!")
        success = True

    except Exception as e:
        conn.rollback()
        st.error(f"Failed to save changes: {e}")

    finally:
        conn.close()

    # Reload the data so the editor reflects the database
    # if success:
    #     st.success("Changes Updated")
        # st.rerun()


st.sidebar.header("First page")

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
        extracted_skills_json = json.dumps([s.strip() for s in extracted_skills.split(',') if s.strip()]) if extracted_skills else "[]"
        insert_application(company, role, date_applied, extracted_skills_json, deadline, status, notes)
        st.success('Form Submitted Succesfully', icon="✅")


