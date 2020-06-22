
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app

CASTING_ASSISTANT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imt0V0xySlhtdVh4ZEc4WlM0WURmRCJ9.eyJpc3MiOiJodHRwczovL2Rldi10bzl1M3lqNi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzMyYmM3ZTAzMzcwMDE0YTU0OTc0IiwiYXVkIjoiY2FzdGluZ19zZXJ2aWNlIiwiaWF0IjoxNTkyODM2ODgxLCJleHAiOjE1OTI5MjMyODEsImF6cCI6ImdMUWJxcEVINXJpYnduYlpKaUdSd1c0QzRSVzRwdXZTIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.NEwcTlpiqeBpxqQ0wQowJ0ORtLp-bU4MYcKTiXfyipCeWl7z8CbyiJiMfBrJ2Yad_NBZvsie13AG5LguTrdbdEU_Bp9G0fbfpmuCriVPkxXkOW6cEVzBDGTkCc2A0tCMQDAomEkWdKefReSBODrDDjJsKTZy2FNsnGqNIwro0Ca8YAvnlI7P703fiqkOpldPOHa_w1uRByK2w4lKrtO8QCPuRAsGW3fnVFcmBuZjP5vitWjQ4BwcEC-n2rwFyDgKl_p43iQAVwxYd2KJWYky2gZ-_fLkjIl3BQK12B09yMUxctLNpV5VeJIBLjrxLk972FjYJUpstdRvt8x-461PrA"
CASTING_DIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imt0V0xySlhtdVh4ZEc4WlM0WURmRCJ9.eyJpc3MiOiJodHRwczovL2Rldi10bzl1M3lqNi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmMDdiODNmYzc0YTIwMDE5ZDM1ZGJkIiwiYXVkIjoiY2FzdGluZ19zZXJ2aWNlIiwiaWF0IjoxNTkyODM2OTczLCJleHAiOjE1OTI5MjMzNzMsImF6cCI6ImdMUWJxcEVINXJpYnduYlpKaUdSd1c0QzRSVzRwdXZTIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGU6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsInJlYWQ6YWN0b3JzIiwicmVhZDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.VjXNfeIUNMWeMwPjkNPTop-fUK8Rd9-ep0AbWODd2nl5K_rhqmUlVkqpJBVpIpALRlL5jlO2o0_jYCzRVFFxXElIo7tTRvWEgJ69zeJsE7B6A_M4PaOZsOwhVcQc90d_DkWFKWBmuXy_TejCyRAqVdl1nLPGdylpi0lPnXcPFAuWGdWqc1kFy_w3saV9IzuXHJPzn8Li8hvWuhErwslQcszaraJkNIIRvCVYywAAhQnlpCpmW9ALTVrfTSthI6x8wGytPrpqXYnJIPug8LTBqDApZbsGfL_RpVdDiMJ4c6yYEaAuCNscO5dWppsznOuS0zstq0ipYPGSXIC0cJt6rg"
PRODUCER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imt0V0xySlhtdVh4ZEc4WlM0WURmRCJ9.eyJpc3MiOiJodHRwczovL2Rldi10bzl1M3lqNi5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTYyNDIwOTI4ODA3MTU0NzMzMzQiLCJhdWQiOlsiY2FzdGluZ19zZXJ2aWNlIiwiaHR0cHM6Ly9kZXYtdG85dTN5ajYuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5MjgzNzA3OCwiZXhwIjoxNTkyOTIzNDc4LCJhenAiOiJnTFFicXBFSDVyaWJ3bmJaSmlHUndXNEM0Ulc0cHV2UyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGU6YWN0b3JzIiwiY3JlYXRlOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.DPNpGKT9wYkVtcTb5PA1b6cd_GSj8dvfJwvev6GhLxOMPOERIpv8C28Ueb7sgSgkgUO3nmdDdFFzsWMqCjRDm3xnmoR2BFMDCfsGP7nSTmRbBw7xxaP634cUqJMRYtHWG1qpyP9kXqQkBZtWJ5T0bWTlcrBq_Ml4A74EFqPdcUj_7h8lhvmn7fT42rS0BkRh9t798WnJwfssp_7yr716eW4wUy9RppL7F0j6nze7zwArkEKCt3TPf0iakIO0LXRd_2qpfhL3P-x6Q7T1HLHmyGLCfOm5ocbIjuzv5_amHe7z1r3mqkO0XL5syT_SgIsqf-nEle4uilk0QeeAwYQ0wA"
INVALID_TOKEN = "ayJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imt0V0xySlhtdVh4ZEc4WlM0WURmRCJ9.eyJpc3MiOiJodHRwczovL2Rldi10bzl1M3lqNi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzMyYmM3ZTAzMzcwMDE0YTU0OTc0IiwiYXVkIjoiY2FzdGluZ19zZXJ2aWNlIiwiaWF0IjoxNTkyODE5MDIzLCJleHAiOjE1OTI5MDU0MjMsImF6cCI6ImdMUWJxcEVINXJpYnduYlpKaUdSd1c0QzRSVzRwdXZTIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.HOMJHksqu7iTKz7WpAAH15x7fOncmv2ZFVApEg0SNcNgShv30ALwFhG40GB8xwR9e_kN_XqjvCUJfRzVehvIfAQguamhXxjC6paGKN8D2ambJVq2xAA4wSkQfSBOEMws2Xqbaft1DOKE8toXTAyORK6idXYBvUN3B-hm5C1CCR41u7hZvvlkFfNv1NZOm8F9ASadT485BgoKEq2ARvRQ3mN1HzO-trHr1tWE2ySVRweXE25BQWQXX9xhM_y90AjtEKAj7IAkc3akEPkNt8fsTRB5pg1x5DbOCWaaq63FwM9OXu6al1MWQmV0HeKDpcop3AolsHVYz9GL8OxJCZEoOg"
EXPIRED_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imt0V0xySlhtdVh4ZEc4WlM0WURmRCJ9.eyJpc3MiOiJodHRwczovL2Rldi10bzl1M3lqNi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVlMzMyYmM3ZTAzMzcwMDE0YTU0OTc0IiwiYXVkIjoiY2FzdGluZ19zZXJ2aWNlIiwiaWF0IjoxNTkyODM2MDIxLCJleHAiOjE1OTI4MzYwMjYsImF6cCI6ImdMUWJxcEVINXJpYnduYlpKaUdSd1c0QzRSVzRwdXZTIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmFjdG9ycyIsInJlYWQ6bW92aWVzIl19.rkNDc_aUAngwuqOvALGUVKE832XmUp5qjjyxRgejBKNXo6my87dU3B1I0y9MO3NybF8evLcRgo5EYt5H7OqaD_JHgOX39fb0UYD9KFI3rA28kvCXUUw6MOyUJS57fSl-U_JvbAGXd8ZepItiZxhYKV7RmYaZ5k80Vk-s0FBRzV5XLaEq4U5txLcJ79P-knIi2PzBWOdZsH9s69PMmFipGwELE-iNiIFHkB3iWoJf8DCxOXZqOJKTys1GmlnopdHOabSK8MnFPZVjNuQeq6FvxuQZ73wxZ2-0KFdv9UmgPy9Hx-MClgI38q7_pQBvDuE0KqaGV74BBBWsYW9Hf-SJnw"


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
    def test_get_actors_assistant_token(self):
        res = self.client().get('/actors/', headers={"Authorization": "Bearer " + CASTING_ASSISTANT_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_get_actors_director_token(self):
        res = self.client().get('/actors/', headers={"Authorization": "Bearer " + CASTING_DIRECTOR_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])
    
    def test_get_actors_director_token(self):
        res = self.client().get('/actors/', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])
    
    def test_get_actors_no_token(self):
        res = self.client().get('/actors/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)


    def test_get_actor_by_a_valid_id(self):
        res = self.client().get('/actors/2', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["actors"])

    def test_404_returned_if_get_actor_by_an_invalid_id(self):
        res = self.client().get('/actors/100', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    def test_create_new_actor_assistant(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1
                    }
        res = self.client().post('/actors', json=new_actor, headers={"Authorization": "Bearer " + CASTING_ASSISTANT_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_create_new_actor_director(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1
                    }
        res = self.client().post('/actors', json=new_actor, headers={"Authorization": "Bearer " + CASTING_DIRECTOR_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
    
    def test_create_new_actor_producer(self):
        new_actor = {
                    "name": "new actor",
                    "age": 5,
                    "gender":1
                    }
        res = self.client().post('/actors', json=new_actor, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
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
        res = self.client().post('/actors', json=new_actor, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
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
        res = self.client().post('/actors', json=new_actor, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
    
    def test_delete_an_valid_actor_assistant(self):
        res = self.client().delete('/actors/9', headers={"Authorization": "Bearer " + CASTING_ASSISTANT_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_delete_an_valid_actor_director(self):
        res = self.client().delete('/actors/9', headers={"Authorization": "Bearer " + CASTING_DIRECTOR_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_an_valid_actor_producer(self):
        res = self.client().delete('/actors/11', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_an_invalid_actor(self):
        res = self.client().delete('/actors/100', headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

    def test_udpate_an_valid_actor_name_assistant(self):
        res = self.client().patch('/actors/2', json={"name" : "test", "movies":[1,2,3,4]}, headers={"Authorization": "Bearer " + CASTING_ASSISTANT_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"], False)

    def test_udpate_an_valid_actor_name_director(self):
        res = self.client().patch('/actors/2', json={"name" : "test", "movies":[1,2,3,4]}, headers={"Authorization": "Bearer " + CASTING_DIRECTOR_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["update"]["name"], "test")

    def test_udpate_an_valid_actor_name_producer(self):
        res = self.client().patch('/actors/2', json={"name" : "test", "movies":[1,2,3,4]}, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["update"]["name"], "test")

    def test_udpate_an_invalid_actor_attribute(self):
        res = self.client().patch('/actors/2', json={"nafddfme" : "test"}, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)

    
    def test_udpate_an_invalid_actor_name(self):
        res = self.client().patch('/actors/200', json={"name" : "test", "movies":[1,2,3,4]}, headers={"Authorization": "Bearer " + PRODUCER_TOKEN})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()