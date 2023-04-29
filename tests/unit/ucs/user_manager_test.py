from app.thirdparties.fs.database_fs import DatabaseFs
from app.ucs.user_manager import UserManager
from app.ucs.use_case_response import Success


def test_create():
    db = DatabaseFs()
    uc = UserManager(db)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    resp = uc.get('avancinirodrigo@gmail.com', 'avancini')
    assert isinstance(resp.type, Success)
    user = resp.data
    assert user.name == 'Rodrigo Avancini'
    assert user.password == 'avancini'
    assert user.email == 'avancinirodrigo@gmail.com'
