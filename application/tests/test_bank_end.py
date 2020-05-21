import unittest
from falsk import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Posts
from os import getenv

