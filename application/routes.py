from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Personality, Songs
from application.quiz import QuestionForm, SongForm



@app.route('/')
@app.route('/home')
def home():
    postData=Songs.query.all()
    return render_template('home.html', title='Home Page', songs=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/quiz', methods=['GET', 'POST'])

def quiz():
    form=QuestionForm()
    if form.validate_on_submit():
        data= Personality(
            name=form.name.data,
            personality_type=form.personality_type.data
        )
        db.session.add(data)
        db.session.commit()
        
        if form.personality_type.data=='Introvert':
            return redirect(url_for('introversion'))
        elif form.personality_type.data=='Extravert':
            return redirect(url_for('extraversion'))

    return render_template('quiz.html', title='Quiz', form=form)

@app.route('/extraversion', methods=['GET', 'POST'])
    
def extraversion():
        form=SongForm()
        if form.validate_on_submit():
            songData=Songs(
                title=form.title.data,
                artist=form.artist.data,
                genre=form.genre.data,
                instrument=form.instrument.data
            )
            db.session.add(songData)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            print(form.errors)
        return render_template('extraversion.html', title='Extraversion Songs', form=form)

@app.route('/new', methods=['GET', 'POST'])
def extraversion_new():
    return render_template('extravert_new.html')

@app.route('/introversion')

def introversion():
    return render_template('introversion.html', title='Introversion Songs')
