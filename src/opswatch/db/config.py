import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

database_url = os.environ["DATABASE_URL"]

engine = create_engine(database_url, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
