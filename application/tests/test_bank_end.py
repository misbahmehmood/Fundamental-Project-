import unittest
from falsk import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Posts
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name='testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'))

def setUp(self):
    db.session.commit()
    db.drop_all()
    db.create_all()