import pytest
from app.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


@pytest.fixture
def alchemydb():
    url = 'postgresql://postgres:postgres@localhost:5432/kofetestdb'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create_all(overwrite=True)
    yield db
    db.close()
    db.drop()
