import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Personality, Songs
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        config_name='testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_URI'),
        SECRET_KEY=getenv('TEST_SECRET_KEY'),
        WTF_CSRF_ENABLE=False,
        DEBUG=True
        )
        return app
    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()
        personality_type1 = Personality(personality_type='Extravert')
        personality_type2 = Personality(personality_type='Introvert')
        db.session.add(personality_type1)
        db.session.add(personality_type2)
        db.session.commit()

    def tearDown(self):

        db.session.remove
        db.drop_all()
 
class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_aboutpage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    def test_extravert_view(self):
        response = self.client.get(url_for('extravert'))
        self.assertEqual(response.status_code, 200)
    def test_introvert_view(self):
        response = self.client.get(url_for('introvert'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):
    def test_redirect_option1(self):
        response= self.client.post('/quiz',
        data=dict(options='Extravert'),
        follow_redirects=True
        )
    def test_redirect_option2(self):
        response= self.client.post('/quiz',
        data=dict(options='Introvert'),
        follow_redirects=True
        )
    def test_adding_post(self):
        response= self.client.post('/extravert',
        data=dict(title='test title',
            artist= 'test artist',
            genre = 'test genre',
            instrument = 'test instrument'),
        follow_redirects=True)
        self.assertIn(b'test title', response.data) 
    def test_adding_post2(self):
        response= self.client.post('/introvert',
        data=dict(title='test title',
                artist= 'test artist',
                genre = 'test genre',
                instrument = 'test instrument'),
            follow_redirects=True)
        self.assertIn(b'test title', response.data) 
        
class TestDelete(TestBase):
    def delete_post(self):
        ids = [a.id for a in Songs]
        assert Songs.count() == 2
        Songs.delete(ids[0])
        assert Songs.count() == 1


