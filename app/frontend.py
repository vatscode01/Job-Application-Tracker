import streamlit as st, sqlite3

from read_application import get_applications, insert_application
from read_application import delete_application

# df = print_applications(True)
df = get_applications()
# df.drop(columns=['id'],inplace=True)

st.title("**Job Application Tracker**")

edited_df = st.data_editor(
    data = df,
    hide_index=True,
    column_config={
        'id': 'ID',
        'company': st.column_config.Column("Company Name", required=True,),
        'role':'Job Role',
        'date_applied':'Date Applied',
        'extracted_skills':'Extracted Skills',
        'deadline':'Deadline',
        'status' : 'Status',
        'notes': 'Notes'
    },
    disabled=['id'],
    num_rows = 'dynamic',
    key = 'editor',
)

if(st.button("Submit")):
    edits = st.session_state["editor"]
    
    conn = sqlite3.connect("database/job_tracker.db")
    
    try:
        # -------------------------
        # Updated cells
        # -------------------------
        for row_idx, changes in edits["edited_rows"].items():
    
            row_id = df.iloc[row_idx]["id"]

            # Only update the columns that actually changed
            for column, new_value in changes.items():

                # Don't allow the primary key to be changed
                if column == "id":
                    continue

                query = f"""
                    UPDATE Applications
                    SET "{colummn}" = ?
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

            row_id = df.iloc[row_idx]["id"]

            conn.execute(
                "DELETE FROM users WHERE id = ?",
                (row_id,)
            )

        # -------------------------
        # Added rows
        # -------------------------
        for row in edits["added_rows"]:
            insert_application('{company}', '{role}', '{date_applied}', '{extracted_skills}', '{deadline}', '{status}', '{notes}')

        conn.commit()
        st.success("Changes saved successfully!")

    except Exception as e:
        conn.rollback()
        st.error(f"Failed to save changes: {e}")

    finally:
        conn.close()

    # Reload the data so the editor reflects the database
    st.rerun()


st.sidebar.markdown('<h1>Frontend</h1>')

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



