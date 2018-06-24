class TennisGame(object):
    def __init__(self, first_player_name, second_player_name):
        self.second_player_name = second_player_name
        self.first_player_name = first_player_name
        self.second_player_score_times = 0
        self.scoreLookup = {0: 'love', 1: 'fifteen', 2: 'thirty', 3: 'forty'}
        self.first_player_score_times = 0

    def score(self):
        if self.is_score_different():
            if self.is_ready_for_win():
                return self.adv_state()

            return self.normal_score()

        if self.is_deuce():
            return self.deuce()

        return self.same_score()

    def same_score(self):
        return self.scoreLookup[self.first_player_score_times] + ' all'

    def deuce(self):
        return 'deuce'

    def is_deuce(self):
        return self.first_player_score_times >= 3

    def is_score_different(self):
        return self.first_player_score_times != self.second_player_score_times

    def is_ready_for_win(self):
        return self.first_player_score_times > 3 or self.second_player_score_times > 3

    def normal_score(self):
        return self.scoreLookup[self.first_player_score_times] + ' ' + self.scoreLookup[
            self.second_player_score_times]

    def adv_state(self):
        return self.adv_player_name() + (' Adv' if self.is_adv() else ' Win')

    def is_adv(self):
        return abs(self.first_player_score_times - self.second_player_score_times) == 1

    def adv_player_name(self):
        return self.first_player_name if self.first_player_score_times > self.second_player_score_times else self.second_player_name

    def first_player_score(self):
        self.first_player_score_times += 1

    def second_player_score(self):
        self.second_player_score_times += 1
