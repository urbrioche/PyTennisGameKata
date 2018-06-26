import unittest

from TennisGame import TennisGame


class TennisGameTest(unittest.TestCase):

    def setUp(self):
        self.game = TennisGame('Joey', 'Tom')

    def test_love_all(self):
        self.score_should_be('love all')

    def test_fifteen_love(self):
        self.game.first_player_score()
        self.score_should_be('fifteen love')

    def test_thirty_love(self):
        self.given_first_player_score(2)
        self.score_should_be("thirty love")

    def test_forty_love(self):
        self.given_first_player_score(3)
        self.score_should_be("forty love")

    def test_love_fifteen(self):
        self.game.second_player_score()
        self.score_should_be("love fifteen")

    def test_love_thirty(self):
        self.given_second_player_score(2)
        self.score_should_be("love thirty")

    def test_fifteen_all(self):
        self.game.second_player_score()
        self.game.first_player_score()
        self.score_should_be("fifteen all")

    def test_thirty_all(self):
        self.given_first_player_score(2)
        self.given_second_player_score(2)
        self.score_should_be("thirty all")

    def test_deuce(self):
        self.given_first_player_score(3)
        self.given_second_player_score(3)
        self.score_should_be("deuce")

    def test_deuce_when_4_4(self):
        self.given_first_player_score(4)
        self.given_second_player_score(4)
        self.score_should_be("deuce")

    def test_first_player_adv(self):
        self.given_first_player_score(4)
        self.given_second_player_score(3)
        self.score_should_be("Joey Adv")

    def test_second_player_adv(self):
        self.given_first_player_score(3)
        self.given_second_player_score(4)
        self.score_should_be("Tom Adv")

    def test_first_player_win(self):
        self.given_first_player_score(3)
        self.given_second_player_score(5)
        self.score_should_be("Tom Win")

    def given_second_player_score(self, times):
        for i in range(times):
            self.game.second_player_score()

    def given_first_player_score(self, times):
        for i in range(times):
            self.game.first_player_score()

    def score_should_be(self, expected):
        score = self.game.score()
        self.assertEqual('%s' % expected, score)


if __name__ == '__main__':
    unittest.main()
