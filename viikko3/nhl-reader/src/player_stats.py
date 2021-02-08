from player_reader import PlayerReader
from player import Player

def sort_by_points(player):
    return player.points

class PlayerStats:

    def __init__(self,player_reader):
        self.players = sorted(player_reader.get_players(), reverse=True, key=sort_by_points)

    def top_scorers_by_nationality(self,nationality):
        return [player for player in self.players if player.nationality==nationality]


