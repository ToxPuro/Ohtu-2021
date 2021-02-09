class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score_equal(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        elif self.m_score1 == 3:
            return "Forty-All"
        else:
            return "Deuce"

    def get_score_40(self):
            minus_result = self.m_score1 - self. m_score2

            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

    def player_score(self,player_points):
        if player_points == 0:
            return "Love"
        if player_points == 1:
            return "Fifteen"
        if player_points == 2:
            return "Thirty"
        return "Forty"

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            return self.get_score_equal()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_40()

        else:
            return self.player_score(self.m_score1) + "-" + self.player_score(self.m_score2)
