from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Personality, Songs
from application.quiz import Questions



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/quiz', methods=['GET', 'POST'])

def quiz():
    form=Questions()
    if form.validate_on_submit():
        data= Personality(
            name=form.name.data,
            personality_type=form.personality_type.data
        )
        db.session.add(data)
        db.session.commit()
        search=Questions(request.form)
        if form.personality_type.data=='Introvert':
            return redirect(url_for('introversion'))
        elif form.personality_type.data=='Extravert':
            return redirect(url_for('extraversion'))

    return render_template('quiz.html', title='Quiz', form=form)

@app.route('/extraversion')
    
def extraversion():

    return render_template('extraversion.html', title='Extraversion Songs', form=Songs)

@app.route('/new', methods=['GET', 'POST'])
def extraversion_new():
    return render_template('extravert_new.html')

@app.route('/introversion')

def introversion():
    return render_template('introversion.html', title='Introversion Songs')
