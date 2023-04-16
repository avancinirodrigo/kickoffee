from thirdparties.fs.database_fs import DatabaseFs
from ucs.user_manager import UserManager


def test_create():
    db = DatabaseFs()
    uc = UserManager(db)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    user = uc.get('avancinirodrigo@gmail.com')
    assert user.name == 'Rodrigo Avancini'
    assert user.password == 'avancini'
    assert user.email == 'avancinirodrigo@gmail.com'
