from unittest.mock import patch
import pytest
from sqlalchemy import exc
from app.entities.user import User
from app.thirdparties.sqlalchemy.sqlalchemy_session import NotNullViolationException
from app.thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


def test_create():
    dbname = 'createdb'
    url = f'postgresql://postgres:postgres@localhost:5432/{dbname}'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create(overwrite=True)
    assert db.exists()
    db.drop()
    db.close()


def test_create_all():
    dbname = 'createalldb'
    url = f'postgresql://postgres:postgres@localhost:5432/{dbname}'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create(overwrite=True)
    db.create_all()

    urepo = db.user_repo()
    user = User('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    session = db.session()
    urepo.add(user, session)
    user_from_repo = urepo.get('avancinirodrigo@gmail.com', session)
    session.close()
    assert user_from_repo.name == 'Rodrigo Avancini'
    assert user_from_repo.password == 'avancini'
    assert user_from_repo.email == 'avancinirodrigo@gmail.com'

    db.close()
    db.drop()


def test_null_exception(alchemydb):
    dbname = 'nullexdb'
    url = f'postgresql://postgres:postgres@localhost:5432/{dbname}'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create(overwrite=True)
    db.create_all()

    urepo = db.user_repo()
    user = User('Rodrigo Avancini', 'avancinirodrigo@gmail.com', None)
    session = db.session()
    with pytest.raises(NotNullViolationException) as e:
        urepo.add(user, session)
    assert str(e.value) == 'Object violates not-null constraint'
    session.close()
    db.close()
    db.drop()


@patch('sqlalchemy.orm.Session.commit',
       side_effect=exc.IntegrityError(None, None, Exception('Test')))
def test_commit_exception(alchemydb):
    dbname = 'nullexdb'
    url = f'postgresql://postgres:postgres@localhost:5432/{dbname}'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create(overwrite=True)
    db.create_all()

    urepo = db.user_repo()
    user = User('Rodrigo Avancini', 'avancinirodrigo@gmail.com', None)
    session = db.session()
    with pytest.raises(Exception) as e:
        urepo.add(user, session)
    assert 'Test' in str(e.value)
    session.close()
    db.close()
    db.drop()


def test_create_overwrite():
    dbname = 'createoverdb'
    url = f'postgresql://postgres:postgres@localhost:5432/{dbname}'
    db = SqlAlchemyDatabase()
    db.connect(url)
    db.create(overwrite=True)
    assert db.exists()
    db.create(overwrite=True)
    assert db.exists()
    db.drop()
    db.close()
