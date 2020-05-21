from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Personality, Songs
from application.forms import PersonalityForm, SongForm, UpdateForm


@app.route('/')
@app.route('/home')
def home():
    
    return render_template('home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/quiz', methods=['GET', 'POST'])

def quiz():
    dataform=PersonalityForm()
    personality_id=dataform.options.data
    if request.method == 'POST':
        
        if dataform.options.data == 'Extravert':
            return redirect(url_for('extravert'))
        else:
            return redirect(url_for('introvert'))

    return render_template('quiz.html', title='Quiz', form=dataform)

@app.route('/extravert', methods=['GET', 'POST'])
def extravert():
        form=SongForm()
        if form.validate_on_submit():
            songData=Songs(
                title=form.title.data,
                artist=form.artist.data,
                genre=form.genre.data,
                instrument=form.instrument.data,
                personality_id=1
            )
            db.session.add(songData)
            db.session.commit()
            return redirect(url_for('extravert_read'))
        else:
            print(form.errors)
        return render_template('extravert.html', title='Songs', form=form)

@app.route('/extravert/read')
def extravert_read():
    postData=Songs.query.filter_by(personality_id=1).all()
    return render_template('extravert_read.html', title='Your Songs', songs=postData)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    to_update= Songs.query.get_or_404(id)
    form=UpdateForm()
    if request.method == 'POST':
        
        if form.validate_on_submit():
            to_update.title=form.title.data,
            to_update.artist=form.artist.data,
            to_update.genre=form.genre.data,
            to_update.instrument=form.instrument.data
            db.session.commit()
            return redirect (url_for('home'))

    return render_template('extravert_new.html', title='Update', form=form, update=to_update)

@app.route('/delete/<int:id>')
def delete(id):
    to_delete= Songs.query.get_or_404(id)
    
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    

@app.route('/introvert', methods=['GET', 'POST'])
def introvert():
        form=SongForm()
        if form.validate_on_submit():
            songData=Songs(
                title=form.title.data,
                artist=form.artist.data,
                genre=form.genre.data,
                instrument=form.instrument.data,
                personality_id=2
                )
            db.session.add(songData)
            db.session.commit()
            return redirect(url_for('introvert_add'))
        else:
            print(form.errors)
        return render_template('introvert.html', title='Your Songs', form=form)
@app.route('/introvert/add')
def introvert_add():
    postData=Songs.query.filter_by(personality_id=2).all()
    return render_template('introvert_add.html', title='See your Songs', songs=postData)

@app.route('/introvert/update/<int:id>', methods=['GET', 'POST'])
def introvert_update(id):
    to_update= Songs.query.get_or_404(id)
    form=UpdateForm()
    if request.method == 'POST':
        
        if form.validate_on_submit():
            to_update.title=form.title.data,
            to_update.artist=form.artist.data,
            to_update.genre=form.genre.data,
            to_update.instrument=form.instrument.data
            db.session.commit()
            return redirect (url_for('introvert_add'))

    return render_template('introvert_update.html', title='Update', form=form, update=to_update)

@app.route('/introvert/delete/<int:id>')
def introvert_delete(id):
    to_delete= Songs.query.get_or_404(id)
    
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('introvert_add'))
