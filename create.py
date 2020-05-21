from application import db
from application.models import Personality, Songs

db.create_all()
post1 = Personality(personality_type = 'Extravert')
post2 = Personality(personality_type = 'Introvert')

db.session.add(post1)
db.session.add(post2)
db.session.commit()