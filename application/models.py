from application import db
from datetime import datetime

class Personality(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    personality_type=db.Column(db.String(9))
    songs= db.relationship('Songs', backref='personality', lazy= 'dynamic')
    def __repr__(self):
        return ''.join([
             'Personality Type: ', self.personality_type
            ])

class Songs(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30), nullable=False)
    artist=db.Column(db.String(30), nullable=False)
    genre=db.Column(db.String(20), nullable=False)
    instrument=db.Column(db.String(20), nullable=False)
    link=db.Column(db.String(40), nullable=False, default='Not Supplied')
    date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    personality_id=db.Column(db.Integer, db.ForeignKey('personality.id'))
    def __repr__(self):
        return ''.join([
            'Song Title: ', self.title, '\r\n',
            'Artist: ', self.artist, '\r\n'
            'Genre: ', self.genre, '\r\n', 
            'Instrument: ', self.instrument, '\r\n',
            'Link: ', self.link, '\r\n',
            'Date Added: ', self.date
            ])
        