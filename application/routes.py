from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import Personality, Songs
from application.forms import PersonalityForm, SongForm, UpdateForm


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
    dataform=PersonalityForm()
    print('------------------------------', dataform.validate_on_submit(), '--------------------------------------')
    if request.method == 'POST':
        print('------------------------------', dataform.options.data, '--------------------------------------')
        if dataform.options.data == 'Extravert':
            return redirect(url_for('personality'))

        
    '''data= Personality(
        personality_type=dataform.options.data
    )
    db.session.add(data)
    db.session.commit()'''
        
    
       

    return render_template('quiz.html', title='Quiz', form=dataform)

@app.route('/personality', methods=['GET', 'POST'])
def personality():
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
        return render_template('personality.html', title='Songs', form=form)

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

    return render_template('personality_new.html', title='Update', form=form, update=to_update)




@app.route('/delete/<int:id>')
def delete(id):
    to_delete= Songs.query.get_or_404(id)
    
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for('home'))
    

