from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class BoggleTests(TestCase):

    # TODO-- write tests for every view function / feature!

    # def setUp(self):

    def test_check_repeat_guess(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['answered'] = ['word','banana','ice', 'of', 'baby']
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertIn('word',session['answered'])
            assert Boggle.check_repeat_guess(Boggle, "word", session['answered']) == True
            self.assertTrue(Boggle.check_repeat_guess(Boggle,'ice', session['answered'])) 
            self.assertFalse(Boggle.check_repeat_guess(Boggle, 'nottheword',session['answered']))


    def test_check_in_words(self):
        self.assertTrue(Boggle.check_in_words(Boggle(), 'word'))
        self.assertFalse(Boggle.check_in_words(Boggle(),'nottheword'))
        self.assertFalse(Boggle.check_in_words(Boggle(), 68))

    def test_check_guess(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['answered'] = ['word']
                session['game_board'] = Boggle().make_board()
                theboard  = session['game_board']
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            # self.assertEqual(Boggle.check_guess(Boggle(),'of'), 'not-on-board') cant know in any instance what the board actually is
            self.assertEqual(Boggle.check_guess(Boggle(), 'asfgh', theboard), 'not-word')

    def test_check_points(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['answered'] = ['word']
                change_session['point_total'] = 0
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(Boggle.check_points(Boggle(),'word', 'ok'), 4)


    def test_play_game(self):
        with app.test_client() as client:
            resp = client.get("/play_game")
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<table id="the_board">', html)

    def test_check(self):
        with app.test_client() as client:
            boggle_game_test  = Boggle()
            with client.session_transaction() as session:
                session['answered'] = ['word']
                session['game_board'] = boggle_game_test.make_board()
            resp = client.get('/check?Guess=word')
            jason = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('msg', jason)


    def test_post_game(self):
        with app.test_client() as client:
            with client.session_transaction() as session:
                session['point_total'] = 10
                session['high_score'] = 12
            resp = client.get('/post-game')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p>Words guessed:</p>', html)


