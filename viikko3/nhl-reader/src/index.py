import requests
from player import Player

def sort_by_points(player):
    return player.points

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()


    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['team'],
            player_dict['goals'], player_dict['assists']
        )

        players.append(player)

    print("Players from FIN 2021-01-04 19:15:32.85661")
    print("")
    players = sorted(players, reverse=True, key=sort_by_points)

    for player in players:
        print(player)

if __name__=='__main__':
    main()