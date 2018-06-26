class TennisGame(object):
    def __init__(self):
        self.second_player_score_time = 0
        self.score_lookup = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty',
        }
        self.first_player_score_time = 0

    def score(self):
        if self.first_player_score_time > 0 or self.second_player_score_time >0:
            return self.score_lookup[self.first_player_score_time]+' '+self.score_lookup[self.second_player_score_time]
        return 'love all'

    def first_player_score(self):
        self.first_player_score_time += 1

    def second_player_score(self):
        self.second_player_score_time += 1
