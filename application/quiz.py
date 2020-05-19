from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp


def personality_query():
    return Personality.query
    
class Questions(FlaskForm):
    name= StringField ('Enter your name', 
    validators= [
        DataRequired(),
        Length(min=3, max=20)
        ])

    personality_type= StringField ('Extrovert/Introvert',
    validators=[DataRequired()
    ])

    submit=SubmitField('Save')