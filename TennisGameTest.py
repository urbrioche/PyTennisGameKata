import unittest

from TennisGame import TennisGame


class TennisGameTest(unittest.TestCase):
    def test_love_all(self):
        game = TennisGame()
        score = game.score()
        self.assertEqual('love all', score)


if __name__ == '__main__':
    unittest.main()
