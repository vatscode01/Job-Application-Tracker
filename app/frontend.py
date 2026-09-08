import streamlit as st, sqlite3, json, pandas as pd
import os, time

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
        'job_description': 'Job Description',
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
                
                if column == "job_description" and isinstance(new_value, str) and not new_value.endswith('.txt') and new_value.strip():
                    company_val = changes.get('company', df.iloc[row_idx]['company'])
                    role_val = changes.get('role', df.iloc[row_idx]['role'])
                    company_val = str(company_val).replace(' ', '_') if company_val else "Unknown"
                    role_val = str(role_val).replace(' ', '_') if role_val else "Unknown"
                    filename = f"{company_val}_{role_val}.txt"
                    filepath = os.path.join("Job Descriptions", filename)
                    with open(filepath, "w") as f:
                        f.write(new_value)
                    new_value = filename
                
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
            job_desc_raw = row.get('job_description', '')
            job_desc_filename = ""
            if job_desc_raw and not job_desc_raw.endswith('.txt'):
                company_val = row.get('company', 'Unknown')
                role_val = row.get('role', 'Unknown')
                company_val = str(company_val).replace(' ', '_') if company_val else "Unknown"
                role_val = str(role_val).replace(' ', '_') if role_val else "Unknown"
                job_desc_filename = f"{company_val}_{role_val}.txt"
                filepath = os.path.join("Job Descriptions", job_desc_filename)
                with open(filepath, "w") as f:
                    f.write(job_desc_raw)
            elif job_desc_raw.endswith('.txt'):
                job_desc_filename = job_desc_raw

            conn.execute("""
                INSERT INTO Applications(company, role, date_applied, extracted_skills, deadline, status, notes, job_description)
                VALUES (?,?,?,?,?,?,?,?)
            """, (
                row.get('company', ''),
                row.get('role', ''),
                row.get('date_applied', ''),
                json.dumps([s.strip() for s in row.get('extracted_skills', '').split(',') if s.strip()]) if row.get('extracted_skills') else "[]",
                row.get('deadline', ''),
                row.get('status', ''),
                row.get('notes', ''),
                job_desc_filename
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
    if success:
        st.success("Changes Updated")
        st.rerun()


st.sidebar.header("First page")

with st.form('application_data',clear_on_submit=True):
    company = st.text_input(label = 'Company Name', placeholder='Enter a valid input')
    role = st.text_input(label = 'Job Role', placeholder='Enter a valid input')
    date_applied = st.date_input(label = 'Date Applied',value = "today")
    extracted_skills = st.text_input(label = 'Extracted Skills', placeholder='Enter a valid input')
    deadline = st.date_input(label = 'Application Deadline', value = "today")
    status = st.selectbox(label= "Select options", options=['Applied','Not Applied','Interviewed','Selected','Not Selected'])
    job_description = st.text_area(label="Job Description", placeholder="Paste the job description here")
    notes = st.text_input(label = 'Notes', placeholder='Enter a valid input')

    submitted = st.form_submit_button("Submit")
    if(submitted):
        job_desc_filename = ""
        if job_description.strip():
            job_desc_filename = f"{str(company).replace(' ', '_')}_{str(role).replace(' ', '_')}.txt"
            filepath = os.path.join("Job Descriptions", job_desc_filename)
            with open(filepath, "w") as f:
                f.write(job_description)

        extracted_skills_json = json.dumps([s.strip() for s in extracted_skills.split(',') if s.strip()]) if extracted_skills else "[]"
        insert_application(company, role, date_applied, extracted_skills_json, deadline, status, notes, job_desc_filename)
        st.success('Form Submitted Succesfully', icon="✅")



st.header("Manage Job Descriptions")
if not df.empty:
    options = df['id'].astype(str) + " - " + df['company'] + " (" + df['role'] + ")"
    selected_option = st.selectbox("Select Application to View/Edit Description", options=options.tolist())
    
    if selected_option:
        selected_id = int(selected_option.split(" - ")[0])
        selected_row = df[df['id'] == selected_id].iloc[0]
        filename = selected_row['job_description']
        
        if filename and str(filename).endswith('.txt'):
            filepath = os.path.join("Job Descriptions", filename)
            if os.path.exists(filepath):
                with open(filepath, "r") as f:
                    desc_content = f.read()
                
                st.download_button("Download Description", data=desc_content, file_name=filename)
                
                with st.form("update_description_form"):
                    updated_text = st.text_area("Edit Description", value=desc_content, height=200)
                    if st.form_submit_button("Update File"):
                        with open(filepath, "w") as f:
                            f.write(updated_text)
                        st.success("File updated successfully!")
                        time.sleep(1)
                        st.rerun()
            else:
                st.warning(f"File {filename} not found.")
        else:
            st.info("No text file found for this application.")