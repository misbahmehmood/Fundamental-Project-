from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp


def personality_query():
    return Personality.query
    
class QuestionForm(FlaskForm):
    name= StringField ('Enter your full name', 
    validators= [
        DataRequired(),
        Length(min=3, max=20)
        ])

    personality_type= StringField ('Extrovert/Introvert',
    validators=[DataRequired()
    ])

    submit=SubmitField('Save')

class SongForm(FlaskForm):
    title= StringField('Song Title',
        validators=[DataRequired(),
    ])
    artist=StringField('Artist',
        validators=[DataRequired()
    ])
    genre=StringField('Genre',
        validators=[DataRequired()
    ])
    instrument=StringField('Instrument',
        validators=[DataRequired()
    ])

    submit=SubmitField('Post')