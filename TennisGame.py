class TennisGame(object):
    def __init__(self):
        self.first_player_score_time = 0

    def score(self):
        if self.first_player_score_time == 2:
            return 'thirty love'
        if self.first_player_score_time == 1:
            return 'fifteen love'
        return 'love all'

    def first_player_score(self):
        self.first_player_score_time +=1
