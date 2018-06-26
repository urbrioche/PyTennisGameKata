import unittest

from TennisGame import TennisGame


class TennisGameTest(unittest.TestCase):

    def setUp(self):
        self.game = TennisGame()

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
        self.game.second_player_score()
        self.game.second_player_score()
        self.score_should_be("love thirty")

    def given_first_player_score(self, times):
        for i in range(times):
            self.game.first_player_score()

    def score_should_be(self, expected):
        score = self.game.score()
        self.assertEqual('%s' % expected, score)


if __name__ == '__main__':
    unittest.main()
