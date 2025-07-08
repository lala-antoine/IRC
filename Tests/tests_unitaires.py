# Ce test vérifie trois comportements : l'inscription, la connexion réussie, et l'échec de connexion avec un mauvais mot de passe

import unittest
import json

class UserServiceTestCase(unittest.TestCase):

    def setUp(self):
        # Créé un client de test
        self.client = test_client()


    def test_register(self):
        # Test d'inscription
        response = self.client.post('/register', json = {
            'pseudo': 'roger',
            'email': 'roger@canaduck.com',
            'password': 'test123'
        })
        self.assertIn(response.status_code, [200, 201])

    def test_login_success(self):
        # S'assurer que le login marche après le register
        self.client.post('/register', json={
            'pseudo': 'roger',
            'email': 'roger@canaduck.com',
            'password': 'test123'
        })
        response = self.client.post('/login', json={
            'pseudo': 'roger',
            'password': 'test123'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("token", data)

    def test_login_wrong_password(self):
        # Mauvais mot de passe donc affiche échec
        self.client.post('/register', json={
            'pseudo': 'roger2',
            'email': 'roger2@canaduck.com',
            'password': 'blabla'
        }
        )
        response = self.client.post('/login', json={
            'pseudo': 'roger2',
            'password': 'passko'
        })
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
