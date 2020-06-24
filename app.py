from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

app.debug = True

debug = DebugToolbarExtension(app)


boggle_game = Boggle()

@app.route('/')
def root():
    return render_template('home.html')