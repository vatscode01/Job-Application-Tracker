# from typing import Optional
# from datetime import date
# from sqlalchemy import create_engine, String, Date
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# # 1. Connect to the database engine
# # SQLite automatically generates the 'example.db' file if it is missing
# engine = create_engine("sqlite:///example.db", echo=True)

# # 2. Define the declarative base class
# class Base(DeclarativeBase):
#     pass

# # 3. Create your database model (Table schema)
# class User(Base):
#     __tablename__ = "applications"
    
#     id: Mapped[int] = mapped_column(primary_key=True)
#     company: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
#     role: Mapped[Optional[str]] = mapped_column(String(50))
#     status: Mapped[Optional[str]] = mapped_column(String(50))
#     date_applied: Mapped[Optional[date]] = mapped_column(Date)
#     notes: Mapped[Optional[str]] = mapped_column(String(100))
#     extracted_skills: Mapped[Optional[str]] = mapped_column(String(100))

# # 4. Generate the database file and tables
# if __name__ == "__main__":
#     # This reads all classes inheriting from Base and builds the tables
#     Base.metadata.create_all(engine)
#     print("Database and tables created successfully!")

from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Date

# engine = create_engine("sqlite:///new_example.db", echo=True)
# engine = create_engine("postgresql+psycopg2://postgres:aady_02@localhost:5432/job_tracker.db, echo = True")
engine = create_engine("postgresql+psycopg2://postgres:aady_02@localhost:5432/job_tracker", echo=True)

meta = MetaData()

# id , company , role , status (applied/interview/offer/
# rejected), date_applied , notes , extracted_skills

applications = Table(
    "applications",
    meta,
    Column('id', Integer, primary_key=True),
    Column('company', String, nullable=False),
    Column('role', String),
    Column('date_applied', Date),
    Column('extracted_skills', String),
    Column('notes', String)
)

meta.create_all(engine)

# conn = engine.connect()



# conn.commit()



