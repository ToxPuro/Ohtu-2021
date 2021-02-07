import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics=Statistics(
            PlayerReaderStub()
        )

    def test_nimi_hakeminen_toimii(self):
        player=self.statistics.search("Semenko")
        self.assertEqual(str(player),"Semenko EDM 4 + 12 = 16")

    def test_joukkueella_hakeminen_toimii(self):
        players=self.statistics.team("EDM")
        self.assertEqual(len(players),3)

    def test_vaaralla_nimella_hakeminen_ei_palauta_mitaan(self):
        player=self.statistics.search("Touko Puro")
        self.assertEqual(player,None)


# En ole varma miksi halutaan kolme pelaajalla 2:n syötteellä, mutta ehkä laskeminen alkaa 0:sta
    def test_parhaimmat_pelaajat(self):
        players=self.statistics.top_scorers(2)
        self.assertEqual(len(players),3)
        self.assertEqual(str(players[0]),"Gretzky EDM 35 + 89 = 124")


    

