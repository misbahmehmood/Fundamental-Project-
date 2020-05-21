from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField 
from application.models import Personality

def personality_query():
    return Personality.query.all()



class PersonalityForm(FlaskForm):

    options= SelectField('Personality', choices=['Introvert','Extravert'])

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

class UpdateForm(FlaskForm):
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

    submit=SubmitField('Update')