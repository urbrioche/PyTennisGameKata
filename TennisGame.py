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
        if self.is_score_different():
            if self.is_ready_for_win():
                return self.adv_player_name() + (' Adv' if self.is_adv() else ' Win')

            return self.normal_score()

        if self.is_deuce():
            return self.deuce()

        return self.same_score()

    def is_deuce(self):
        return self.first_player_score_time >= 3

    def normal_score(self):
        return self.score_lookup[self.first_player_score_time] + ' ' + self.score_lookup[
            self.second_player_score_time]

    def is_adv(self):
        return abs(self.first_player_score_time - self.second_player_score_time) == 1

    def is_ready_for_win(self):
        return self.first_player_score_time > 3 or self.second_player_score_time > 3

    def is_score_different(self):
        return self.first_player_score_time != self.second_player_score_time

    def deuce(self):
        return 'deuce'

    def same_score(self):
        return self.score_lookup[self.first_player_score_time] + ' all'

    def adv_player_name(self):
        return self.first_player_name if self.first_player_score_time > self.second_player_score_time else self.second_player_name

    def first_player_score(self):
        self.first_player_score_time += 1

    def second_player_score(self):
        self.second_player_score_time += 1
