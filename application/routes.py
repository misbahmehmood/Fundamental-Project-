from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Personality, Songs
from application.forms import QuestionForm, SongForm, UpdateForm



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
    dataform=QuestionForm()
    if dataform.validate_on_submit():
        data= Personality(
            name=dataform.name.data,
            personality_type=dataform.personality_type.data
        )
        db.session.add(data)
        db.session.commit()
        
        if dataform.personality_type.data=='Introvert':
            return redirect(url_for('introversion'))
        elif dataform.personality_type.data=='Extravert':
            return redirect(url_for('extraversion'))

    return render_template('quiz.html', title='Quiz', form=dataform)

@app.route('/extraversion', methods=['GET', 'POST'])
    
def extraversion():
        form=SongForm()
        if form.validate_on_submit():
            songData=Songs(
                title=form.title.data,
                artist=form.artist.data,
                genre=form.genre.data,
                instrument=form.instrument.data
                #personality=QuestionForm.personality_type
            )
            db.session.add(songData)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            print(form.errors)
        return render_template('extraversion.html', title='Extraversion Songs', form=form)

@app.route('/extraversion/update', methods=['GET', 'POST'])
def update():
    form=UpdateForm()
    if form.validate_on_submit():
            title=form.title.data,
            artist=form.artist.data,
            genre=form.genre.data,
            instrument=form.instrument.data
            db.session.commit()
            return redirect (url_for('home'))
    return render_template('extraversion_new.html', title='Update', form=form)




@app.route('/delete/<int:id>')
def delete(id):
    to_delete= Songs.query.get_or_404(id)
    
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    


@app.route('/introversion')

def introversion():
    return render_template('introversion.html', title='Introversion Songs')
