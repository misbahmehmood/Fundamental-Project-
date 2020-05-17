from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/extraversion')
def extraversion():
    return render_template('extraversion.html', title='Extraversion Songs')

@app.route('/introversion')
def introversion():
    return render_template('introversion.html', title='Introversion Songs')
