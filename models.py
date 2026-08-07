import sqlite3, pandas as pd

conn = sqlite3.connect("job_tracker.db")

table_name = "applications"
data = pd.read_sql_query(f"select * from {table_name};", conn)

data.to_json("outputs.json", orient='records', indent=4)

conn.close()