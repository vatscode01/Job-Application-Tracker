
# Create Database

import sqlite3, pandas as pd

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

def insert_application(company=None, role=None, date_applied=None, extracted_skills=None, deadline=None, status = None, notes= None):

    if not isinstance(company,str):
        raise TypeError(f"Expected string type but got {type(company).__name__}")
    
    cur.execute("""
        insert into Applications(company, role, date_applied, extracted_skills, deadline, status, notes)
        values (?,?,?,?,?,?,?);
    """,(company, role, date_applied, extracted_skills, deadline, status, notes))
    conn.commit() 

def get_applications(id):
    cur.execute(f"select * from Applications where id={id};")
    row = cur.fetchone()
    print(row)

def update_application(id, company, role, date_applied, extracted_skills, deadline, status, notes):
    cur.execute(f"update Applications set company='{company}',role='{role}', date_applied='{date_applied}', extracted_skills='{extracted_skills}', deadline='{deadline}', status='{status}', notes='{notes}' where id={id};")
    conn.commit()

def delete_application(id):
    cur.execute(f"delete from Applications where id={id}")
    conn.commit()

# Not useful
def print_applications():
    cur.execute("select * from Applications;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # return pd.DataFrame(rows)


create_table("Applications")
# update_application(3,'Google','SWE','2025-06-15',None,'2025-09-05','Not Applied','NA')
# insert_application('Google','SWE','2025-06-15',None,'2025-09-05','Not Applied','NA')
# print_applications(False)