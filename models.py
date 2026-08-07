from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Date, JSON

engine = create_engine("sqlite:///job_tracker.db", echo = True)
meta = MetaData()

# id , company , role , status (applied/interview/offer/
# rejected), date_applied , notes , extracted_skills

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

# insert_statement = applications.insert().values(
#     'Amazon', 'SDE', 'Applied', '2025-05-03', ['Python','AWS'], 'NA'
# )
# I have entered 3 more values into the applications table directly from terminal.

# conn.execute(insert_statement)

from sqlalchemy import text

select_statement = text('select * from applications;')
print(conn.execute(select_statement))

conn.commit()



