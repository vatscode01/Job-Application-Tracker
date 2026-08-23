
# Create Database

import sqlite3

conn = sqlite3.connect("database/job_tracker.db")
cur = conn.cursor()

def create_table(table_name):
    cur.execute(f"""
        create table if not exists {table_name}(
        id INTEGER primary key,
        company TEXT NOT NULL,
        role TEXT,
        date_applied DATE,
        extracted_skills JSON,
        deadline DATE,
        status TEXT,
        notes TEXT)
    """)
    conn.commit()

def insert_application(company, role=str, date_applied=None, extracted_skills=None, deadline=None, status = None, notes= None):
    cur.execute("""
        insert into Applications(company, role, date_applied, extracted_skills, deadline, status, notes)
        values (?,?,?,?,?,?,?);
    """,(company, role, date_applied, extracted_skills, deadline, status, notes))
    # conn.commit

def get_applications():
    cur.execute("select * from Applications;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

create_table("Applications")
insert_application('Google','2025-06-15','2025-08-05','Not Applied','NA')
get_applications()
