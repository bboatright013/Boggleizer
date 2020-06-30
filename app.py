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

    session['high_score'] = 0
    session['games_played'] = 0
    return render_template('main.html')

@app.route('/play_game')
def play_game():
    session['game_board'] = boggle_game.make_board()
    session['answered'] = []
    session['point_total'] = 0
    return render_template('home.html')

@app.route('/check')
def check():
    guess = request.args.get("Guess")
    alist = session['answered']
    theboard = session['game_board']

    if boggle_game.check_in_words(guess) != True: 
        res = boggle_game.check_guess(guess, theboard)
        return jsonify(msg="Not Scorable",
                        res = res)
    if boggle_game.check_repeat_guess(guess,  alist) == True:
        res = boggle_game.check_guess(guess,theboard)
        return jsonify(msg="already guessed that one mate",
                        res = res)
    res = boggle_game.check_guess(guess, theboard)
    points = boggle_game.check_points(guess, res)
    return jsonify(msg="Good Find!",
                    res = res,
                    points = points)

@app.route('/post-game')
def post_game():
    if session['point_total'] > session['high_score']:
        session['high_score'] = session['point_total']        
    return render_template('/post-game.html')

@app.route("/post-score")
def post_score():
    games = session.get("games_played", 0)
    session['games_played'] = games + 1

    return redirect('/post_game')