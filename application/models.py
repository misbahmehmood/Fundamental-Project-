from application import db

class Personality(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20), nullable=False)
    personality_type=db.Column(db.String(9), nullable=False)
    songs= db.relationship('Songs', backref='personality')
    def __repr__(self):
        return ''.join([
             'Personality Type: ', self.personality_type, '\r\n',
             'Name: ', self.name
            ])
class Songs(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    song_title=db.Column(db.String(30), nullable=False)
    genre=db.Column(db.String(20), nullable=False)
    length=db.Column(db.Integer, nullable=False)
    personality_id=db.Column(db.Integer, db.ForeignKey('personality.id'))
    def __repr__(self):
        return ''.join([
            'Song Title: ', self.song_title, '\r\n',
            'Genre: ', self.genre, '\r\n', self.length
            ])