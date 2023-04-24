from entities.user import User
from thirdparties.sqlalchemy.sqlalchemy_database import SqlAlchemyDatabase


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
