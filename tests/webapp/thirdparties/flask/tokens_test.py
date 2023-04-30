def test_login_happy_path(app, client):
    signup_data = {'name': 'Rodrigo Avancini',
                   'email': 'avancinirodrigo@gmail.com',
                   'password': 'avancini'}
    client.post('/users', json=signup_data)

    login_data = {'email': 'avancinirodrigo@gmail.com',
                  'password': 'avancini'}
    resp = client.post('/tokens', json=login_data)
    assert resp.status_code == 200
    assert 'token' in resp.json
