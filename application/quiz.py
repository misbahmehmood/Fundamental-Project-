from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Questions(FlaskForm):
    name= StringField ('Enter your name', 
    validators= [
        DataRequired(),
        Length(min=3, max=20)
    ]
    )
    personality_type= 