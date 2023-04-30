def test_signup_happy_path(app, client):
    data = {'name': 'Rodrigo Avancini',
            'email': 'avancinirodrigo@gmail.com',
            'password': 'avancini'}
    resp = client.post('/users', json=data)
    assert resp.status_code == 201