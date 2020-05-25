from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField 
from application.models import Personality


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
    link=StringField('Link')
    
    submit=SubmitField('Post')
    
    def link_url(lst):
        videos=[]
        for link in lst:
            video= 'https://youtube.com/embed/' + link
            videos.append(video)
        return videos


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
    link=StringField('Link',
        validators=[DataRequired()
        ])

    submit=SubmitField('Update')