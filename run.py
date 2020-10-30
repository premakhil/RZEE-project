from flask import Flask, redirect, render_template, url_for
from Database import db

cursor = db.cursor()


app = Flask(__name__)

questions = {
    'Mohammed': 'Is he the best in business when it comes to any f*king sport out there?',
    'Ashoor': 'Will he be the one to soon hit a million in cash?',
    'Shebeeb': 'Is he the fastest of the clan?',
    'Fuad': 'Does he have the ability to turn anything into "A"',
    'Adam': 'Did he almost have the chance of joining Blasters F C ',
    'Allan': 'Always High af?',
    'Akhil': 'Did he develop this site?'
}

global options
options = ['Mohammed', 'Ashoor', 'Shebeeb', 'Fuad', 'Adam', 'Allan', 'Akhil']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/go')
def go():
    return render_template('gopage.html')


@app.route('/play')
def play():
    global options

    for i in options:
        q = questions[i]
        options.remove(i)
        break

    if len(options) == 0:

        options = ['Mohammed', 'Ashoor', 'Shebeeb',
                   'Fuad', 'Adam', 'Allan', 'Akhil']

    return render_template('play.html', q=q)
