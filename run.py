from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/go')
def go():
    return render_template('gopage.html')


@app.route('/play')
def play():
    return render_template('play.html')
