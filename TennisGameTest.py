import unittest

from TennisGame import TennisGame


class TennisGameTest(unittest.TestCase):
    def setUp(self):
        self.tennis_game = TennisGame('Joey', 'Tom')

    def test_love_all(self):
        self.score_should_be('love all')

    def test_fifteen_love(self):
        self.tennis_game.first_player_score()
        self.score_should_be('fifteen love')

    def test_thirty_love(self):
        self.given_first_player_score_time(2)
        self.score_should_be('thirty love')

    def test_forty_love(self):
        self.given_first_player_score_time(3)
        self.score_should_be('forty love')

    def test_love_fifteen(self):
        self.tennis_game.second_player_score()
        self.score_should_be('love fifteen')

    def test_love_thirty(self):
        self.given_second_player_score_times(2)
        self.score_should_be('love thirty')

    def test_fifteen_all(self):
        self.tennis_game.first_player_score()
        self.tennis_game.second_player_score()
        self.score_should_be('fifteen all')

    def test_thirty_all(self):
        self.given_first_player_score_time(2)
        self.given_second_player_score_times(2)
        self.score_should_be('thirty all')

    def test_deuce(self):
        self.given_first_player_score_time(3)
        self.given_second_player_score_times(3)
        self.score_should_be('deuce')

    def test_deuce_when_4_4(self):
        self.given_first_player_score_time(4)
        self.given_second_player_score_times(4)
        self.score_should_be('deuce')

    def test_first_player_advantage(self):
        self.given_first_player_score_time(4)
        self.given_second_player_score_times(3)
        self.score_should_be('Joey Adv')

    def test_second_player_advantage(self):
        self.given_first_player_score_time(3)
        self.given_second_player_score_times(4)
        self.score_should_be('Tom Adv')

    def test_second_player_advantage(self):
        self.given_first_player_score_time(3)
        self.given_second_player_score_times(5)
        self.score_should_be('Tom Win')

    def given_second_player_score_times(self, times):
        for i in range(times):
            self.tennis_game.second_player_score()

    def given_first_player_score_time(self, times):
        for i in range(times):
            self.tennis_game.first_player_score()





    def score_should_be(self, expected='love all'):
        score = self.tennis_game.score()
        self.assertEqual('%s' % expected, score)


if __name__ == '__main__':
    unittest.main()
