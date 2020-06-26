from boggle import Boggle
from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

app.debug = True

debug = DebugToolbarExtension(app)


boggle_game = Boggle()

@app.route('/')
def root():
    session['game_board'] = boggle_game.make_board()
    session['answered'] = []
    session['point_total'] = 0
    return render_template('main.html')

@app.route('/play_game')
def play_game():
    return render_template('home.html')

@app.route('/check')
def check():
    guess = request.args.get("Guess")

    if check_in_words(guess) != True: 
        res = check_guess(guess)
        return jsonify(msg="Not Scorable",
                        res = res)
    if check_repeat_guess(guess) == True:
        res = check_guess(guess)
        return jsonify(msg="already guessed that one mate",
                        res = res)
    res = check_guess(guess)
    points = check_points(guess, res)
    return jsonify(msg="Good Find!",
                    res = res,
                    points = points)



def check_repeat_guess(guess):
    for word in session['answered']:
        if word == guess:
            return True
    return False

def check_in_words(guess):
    for word in boggle_game.words:
        if word == guess:
            return True
    return False

def check_guess(guess):
    res = boggle_game.check_valid_word(session['game_board'], guess)
    answered = session['answered']
    answered.append(guess)
    session['answered'] = answered
    return res

def check_points(guess, res):
    points = 0
    if res == 'ok':
        for char in guess:
            points = points + 1
    # tmp_points = session['point_total']
    # tmp_points = tmp_points + points
    # session['point_total'] = tmp_points
    return points
