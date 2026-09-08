import sys
import sqlite3
import os

sys.path.append('.')
from read_application import insert_application

try:
    print("Testing insert_application with job_description...")
    insert_application("TestCorp", "TestRole", "2026-09-01", "[]", "2026-09-10", "Applied", "Test notes", "test_file.txt")
    print("Insert successful.")
    
    print("Checking database...")
    conn = sqlite3.connect("database/job_tracker.db")
    cur = conn.cursor()
    cur.execute("SELECT job_description FROM Applications WHERE company='TestCorp'")
    row = cur.fetchone()
    print(f"Database job_description value: {row[0]}")
    conn.close()

    if row[0] == "test_file.txt":
        print("Verification PASSED.")
    else:
        print("Verification FAILED.")

except Exception as e:
    print(f"Error during testing: {e}")
