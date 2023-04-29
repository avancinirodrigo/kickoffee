from app.ucs.user_manager import UserManager
from app.ucs.use_case_response import Created, NotFound, Success


def test_create(alchemydb):
    uc = UserManager(alchemydb)
    create_resp = uc.create(
        'Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    assert isinstance(create_resp.type, Created)
    get_resp = uc.get('avancinirodrigo@gmail.com', 'avancini')
    assert isinstance(get_resp.type, Success)
    user = get_resp.data
    assert user.name == 'Rodrigo Avancini'
    assert user.password == 'avancini'
    assert user.email == 'avancinirodrigo@gmail.com'


def test_delete(alchemydb):
    uc = UserManager(alchemydb)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    uc.delete('avancinirodrigo@gmail.com')
    resp = uc.get('avancinirodrigo@gmail.com', 'avancini')
    assert isinstance(resp.type, NotFound)
    assert resp.data is None


def test_update(alchemydb):
    uc = UserManager(alchemydb)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    resp = uc.get('avancinirodrigo@gmail.com', 'avancini')
    user = resp.data
    user.name = user.name + ' Souza'
    user.email = user.email + '.br'
    user.password = user.password + 'souza'
    uc.update('avancinirodrigo@gmail.com', user)
    resp = uc.get('avancinirodrigo@gmail.com.br', 'avancinisouza')
    userUp = resp.data
    assert userUp.name == 'Rodrigo Avancini Souza'
    assert userUp.password == 'avancinisouza'
    assert userUp.email == 'avancinirodrigo@gmail.com.br'
