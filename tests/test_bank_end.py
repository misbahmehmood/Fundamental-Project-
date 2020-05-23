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
        WTF_CSRF_ENABLED=False,
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
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
    def test_extravert_view(self):
        response = self.client.get(url_for('extravert'))
        self.assertEqual(response.status_code, 200)
    def test_introvert_view(self):
        response = self.client.get(url_for('introvert'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):
    def test_redirect(self):
        with self.client:
            response=self.client.post('quiz',
                data=dict(options='Extravert'),
                follow_redirects=True
            )
            self.assertIn(b'+Add a Song', response.data)

    def test_adding_post(self):
        response=self.client.post('/extravert',
        data=dict(title='test title',
            artist='test artist',
            genre= 'test genre',
            instrument='test instrument',
            link= 'test link'),
            follow_redirects=True)
        self.assertIn(b'test title', response.data)
    '''with self.client:
            response= self.client.get(url_for('extravert/read'),
        self.assertEqual(response.status_code, 200))'''
    '''with self.client:
            response=self.client.get(url_for())
            self.assertEqual(response.status_code, 200)'''
        
    

    '''with self.client:
            response=self.client.get('extravert/read')
            self.assertEqual(response.status_code, 200)
        with self.client:
            response=self.client.get (url_for('update', id=1))
            self.assertEqual(response.status_code, 200)
        with self.client:
            response= self.client.post('extravert',
            data=dict(title='test title',
                artist= 'test artist',
                genre = 'test new genre',
                instrument = 'test instrument',
                link = 'link'),
            follow_redirects=True)
            self.assertIn(b'test new genre', response.data)'''


        
class TestDelete(TestBase):
    def delete_post(self):
        response=self.client.post('/extravert',
        data=dict(title='test title',
            artist='test artist',
            genre= 'test genre',
            instrument='test instrument',
            link= 'test link'),
        follow_redirects=True)
        self.assertIn(b'test title', response.data)
        with self.client:
            response= self.client.get(url_for('delete', id=1))
            follow_redirects=True
            self.assertEqual(Songs.query.count(),0)


