import sqlalchemy as db
from models import Applicatiions
from sqlalchemy_utils import database_exits, create_database

print(db.__version__)

engine = db.create_engine(
    "postgresql://postgres:aady_02@localhost:5432/postgres"
)

if not database_exists(engine.url):
    create_database(engine.url)


print(db.select(Applications))

