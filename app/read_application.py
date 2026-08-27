import sqlite3, pandas as pd

def get_applications():
    conn = sqlite3.connect("database/job_tracker.db")

    df = pd.read_sql_query("select * from Applications", conn)
    conn.close()
    return df