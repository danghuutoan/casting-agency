
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app



class ActorTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get("DATABASE_URL")  
       
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # setup_db(self.app, self.database_path)
        from app.mod_actor.controllers import mod_actor as actor_module
        self.app.register_blueprint(actor_module)

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_actors(self):
        res = self.client().get('/actors/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_get_actor_by_a_valid_id(self):
        res = self.client().get('/actors/2')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_404_returned_if_get_actor_by_an_invalid_id(self):
        res = self.client().get('/actors/100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    def test_create_new_actor(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1
                    }
        res = self.client().post('/actors', json=new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_create_new_actor_with_an_available_movie(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1,
                    "movies":[1]
                    }
        res = self.client().post('/actors', json=new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
    
    def test_create_new_actor_with_an_unavailable_movie(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1,
                    "movies":[100]
                    }
        res = self.client().post('/actors', json=new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
    
    def test_delete_an_valid_actor(self):
        res = self.client().delete('/actors/10')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_an_invalid_actor(self):
        res = self.client().delete('/actors/100')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    def test_udpate_an_valid_actor_name(self):
        res = self.client().patch('/actors/2', json={"name" : "test", "movies":[1,2,3,4]})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["update"]["name"], "test")

    def test_udpate_an_invalid_actor_attribute(self):
        res = self.client().patch('/actors/2', json={"nafddfme" : "test"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)

    
    def test_udpate_an_invalid_actor_name(self):
        res = self.client().patch('/actors/200', json={"name" : "test", "movies":[1,2,3,4]})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()