from ucs.user_manager import UserManager


def test_create(alchemydb):
    uc = UserManager(alchemydb)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    user = uc.get('avancinirodrigo@gmail.com')
    assert user.name == 'Rodrigo Avancini'
    assert user.password == 'avancini'
    assert user.email == 'avancinirodrigo@gmail.com'


def test_delete(alchemydb):
    uc = UserManager(alchemydb)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    uc.delete('avancinirodrigo@gmail.com')
    user = uc.get('avancinirodrigo@gmail.com')
    assert user is None


def test_update(alchemydb):
    uc = UserManager(alchemydb)
    uc.create('Rodrigo Avancini', 'avancinirodrigo@gmail.com', 'avancini')
    user = uc.get('avancinirodrigo@gmail.com')
    user.name = user.name + ' Souza'
    user.email = user.email + '.br'
    user.password = user.password + 'souza'
    uc.update('avancinirodrigo@gmail.com', user)
    userUp = uc.get('avancinirodrigo@gmail.com.br')
    assert userUp.name == 'Rodrigo Avancini Souza'
    assert userUp.password == 'avancinisouza'
    assert userUp.email == 'avancinirodrigo@gmail.com.br'
