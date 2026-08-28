import sqlite3, pandas as pd

def get_applications():
    conn = sqlite3.connect("database/job_tracker.db")

    df = pd.read_sql_query("select * from Applications", conn)
    conn.close()
    return df

def insert_application(company=None, role=None, date_applied=None, extracted_skills=None, deadline=None, status = None, notes= None):
    conn = sqlite3.connect("database/job_tracker.db")
    cur = conn.cursor()
    if not isinstance(company,str):
            raise TypeError(f"Expected string type but got {type(company).__name__}")
        
    cur.execute("""
        insert into Applications(company, role, date_applied, extracted_skills, deadline, status, notes)
        values (?,?,?,?,?,?,?);
    """,(company, role, date_applied, extracted_skills, deadline, status, notes))
    conn.commit() 
    conn.close()
    pass