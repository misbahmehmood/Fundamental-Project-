from application import db

class Personality(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    personality_type=db.Column(db.String(9))
    songs= db.relationship('Songs', backref='personality')
    def __repr__(self):
        return ''.join([
             'Personality Type: ', self.personality_type, '\r\n',
             'Name: ', self.name
            ])

class Songs(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30), nullable=False)
    artist=db.Column(db.String(30), nullable=False)
    genre=db.Column(db.String(20), nullable=False)
    instrument=db.Column(db.String(20), nullable=False)
    personality_id=db.Column(db.Integer, db.ForeignKey('personality.id'))
    def __repr__(self):
        return ''.join([
            'Song Title: ', self.title, '\r\n',
            'Artist: ', self.artist, '\r\n'
            'Genre: ', self.genre, '\r\n', 
            'Instrument: ', self.instrument
            ])
        