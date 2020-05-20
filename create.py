from application import db
from application.models import Personality, Songs

db.drop_all()
db.create_all()