
# Create Database

import sqlite3

conn = sqlite3.connect("database/job_tracker.db")

cur = conn.cursor()

cur.execute("create table applications(" \
"id: integer," \
")")

