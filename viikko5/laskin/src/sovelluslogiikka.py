class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.aikaisempi_tulos=0

    def miinus(self, arvo):
        self.aikaisempi_tulos=self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.aikaisempi_tulos=self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.aikaisempi_tulos=self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.aikaisempi_tulos=self.tulos
        self.tulos = arvo

    def kumoa(self):
        self.tulos=self.aikaisempi_tulos

