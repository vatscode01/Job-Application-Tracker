import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE Applications (id INTEGER, name TEXT)")
conn.execute("INSERT INTO Applications VALUES (1, 'Test')")

df = pd.read_sql_query("SELECT * FROM Applications", conn)
row_id = df.iloc[0]["id"]
print("Type of row_id:", type(row_id))
try:
    conn.execute("UPDATE Applications SET name = ? WHERE id = ?", ('New', row_id))
    print("Success without int cast")
except Exception as e:
    print("Error:", e)

