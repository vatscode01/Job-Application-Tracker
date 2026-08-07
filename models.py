from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Date, JSON, text
import sqlite3, json

engine = create_engine("sqlite:///job_tracker.db", echo = True)
meta = MetaData()

applications = Table(
    "applications",
    meta,
    Column('id', Integer, primary_key=True),
    Column('company', String, nullable=False),
    Column('role', String),
    Column('status', String),       #(applied/interview/offer/rejected)
    Column('date_applied', Date),
    Column('extracted_skills', JSON),
    Column('notes', String, nullable=True)      #Default = True
)

meta.create_all(engine)
conn = engine.connect()

conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("select * from job_tracker;")
rows = cursor.fetchall()

data = [dict(row) for row in rows]
with open("output.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)

conn.close()
