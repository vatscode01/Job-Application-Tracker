
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


def get_applications():
    cur.execute("select * from Applications;")
    row = cur.fetchall()
    print(row)

# def insert_application(id, company, role, date_applied, extracted_skills, deadline, status, notes):
#     cur.execute(f"""
#         insert into Applications values({id},{company},{role},{status},{date_applied},{extracted_skills},{deadline},{status},{notes})
#     """)
#     conn.commit();

def insert_application():
    cur.execute(f"""
        insert into Applications values
        (1,'Amazon','SDE','2025-05-03','["Python","AWS"]','2025-08-05','Applied','NA')
    """)
    conn.commit();

create_table("Applications")
get_applications()
# insert_application(1,'Amazon','SDE','2025-05-03','["Python","AWS"]','2025-08-05','Applied','NA')