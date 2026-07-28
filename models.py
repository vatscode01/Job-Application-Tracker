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

from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///mydatabase.db", echo = True)

conn = engine.connect()

conn.execute(text("create table if not exists application (company str , role str , status str);"))

conn.commit()



