from sqlalchemy import text
from sqlmodel import Session

from opswatch.db.config import engine, get_session


def test_db_connection() -> None:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    assert result.scalar_one() == 1


def test_get_session():
    session = get_session()
    value = next(session)

    assert isinstance(value, Session)

    session.close()
