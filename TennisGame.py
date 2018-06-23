class TennisGame(object):

    def __init__(self, first_player_name, second_player_name):
        self.first_player_name = first_player_name
        self.second_player_name = second_player_name
        self.second_player_score_times = 0
        self.first_player_score_times = 0
        self.score_lookup = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty',
        }

    @property
    def score(self):
        if self.is_score_different():
            if self.is_ready_for_win():
                return self.adv_state()
            return self.normal_score()

        if self.is_deuce():
            return 'deuce'
        return self.same_score()

    def same_score(self):
        return self.score_lookup[self.first_player_score_times] + ' all';

    def is_deuce(self):
        return self.first_player_score_times >= 3

    def adv_state(self):
        return self.adv_player() + (' Adv' if self.is_adv() else ' Win')

    def is_score_different(self):
        return self.first_player_score_times != self.second_player_score_times

    def is_ready_for_win(self):
        return self.first_player_score_times > 3 or self.second_player_score_times > 3

    def normal_score(self):
        return self.score_lookup[self.first_player_score_times] + ' ' + self.score_lookup[
            self.second_player_score_times]

    def is_adv(self):
        return abs(self.first_player_score_times - self.second_player_score_times) == 1

    def adv_player(self):
        return self.first_player_name if self.first_player_score_times > self.second_player_score_times else self.second_player_name

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1
