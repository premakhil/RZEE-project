from flask import Flask, redirect, render_template, url_for


app = Flask(__name__)

questions = {
    'Mohammed': 'Is he the best in business when it comes to any f*king sport out there?',
    'Ashoor': "Asma's Habibi?",
    'Shebeeb': 'Is he the fastest of the clan?',
    'Fuad': 'Does he have the ability to sexualize anything?',
    'Adam': 'Did he almost have the chance of joining Blasters?',
    'Allan': 'Bow wow?',
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

    return render_template('play.html', q=q, questions=questions)


@app.route('/mohammed')
def mohammed():

    return render_template('mohammed.html')


@app.route('/ashoor')
def ashoor():
    return render_template('ashoor.html')


@app.route('/shebeeb')
def shebeeb():
    return render_template('shebeeb.html')


@app.route('/fuad')
def fuad():
    return render_template('fuad.html')


@app.route('/adam')
def adam():
    return render_template('adam.html')


@app.route('/allan')
def allan():
    return render_template('allan.html')


@app.route('/akhil')
def akhil():
    return render_template('akhil.html')
