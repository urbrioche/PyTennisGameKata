class TennisGame(object):
    def __init__(self, first_player_name, second_player_name):
        self.second_player_name = second_player_name
        self.first_player_name = first_player_name
        self.second_player_score_time = 0
        self.score_lookup = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty',
        }
        self.first_player_score_time = 0

    def score(self):
        if self.first_player_score_time != self.second_player_score_time:
            if self.first_player_score_time > 3:
                if abs(self.first_player_score_time - self.second_player_score_time)==1:
                    return self.first_player_name + ' Adv'
            return self.score_lookup[self.first_player_score_time]+' '+self.score_lookup[self.second_player_score_time]

        if self.first_player_score_time >= 3:
            return 'deuce'
        return self.score_lookup[self.first_player_score_time]+' all'

    def first_player_score(self):
        self.first_player_score_time += 1

    def second_player_score(self):
        self.second_player_score_time += 1
