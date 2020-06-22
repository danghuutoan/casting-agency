
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app



class TriviaTestCase(unittest.TestCase):
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

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()