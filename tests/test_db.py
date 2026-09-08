import sqlite3
import pandas as pd
import numpy as np, os

conn = sqlite3.connect(":memory:")
conn.execute("Create table Applications (id integer, jd text);")
conn.execute("INSERT INTO Applications VALUES (1, 'Hi, this is a Test file.')")

df = pd.read_sql_query("select * from Applications;", conn)
conn.commit()


# def save_jd():
#     for i in range(0,len(df)):
#         path = f"Job Descripions/file_{df['id'].iloc[i]}"

#         with open(path, 'w') as f:
#             f.write(f"{df['jd'].iloc[i]}")
        

os.makedirs('Job Descriptions', exist_ok=True)
def save_jd(row):
    path = f"output_files/file_{row['id']}.txt"

    with open(path,'w') as f:
        f.write(str(row['jd']))

    return path

df['jd_file'] = df.apply(save_jd, axis = 1)

print(df)


# conn.execute("CREATE TABLE Applications (id INTEGER, name TEXT)")

# df = pd.read_sql_query("SELECT * FROM Applications", conn)
# row_id = df.iloc[0]["id"]
# print("Type of row_id:", type(row_id))
# try:
#     conn.execute("UPDATE Applications SET name = ? WHERE id = ?", ('New', row_id))
#     print("Success without int cast")
# except Exception as e:
#     print("Error:", e)

