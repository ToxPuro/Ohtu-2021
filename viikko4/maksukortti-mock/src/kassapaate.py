HINTA = 5


class Kassapaate:
    def __init__(self):
        self.myytyja_lounaita = 0

    def lataa(self, kortti, summa):
        ## Oletin, että 0 lasketaan tässä tapauksessa positiiviseksi, sillä toinen tapaus oli negatiivinen luku
        if summa >= 0:
            kortti.lataa(summa)

    def osta_lounas(self, kortti):
        if kortti.saldo >= HINTA:
            kortti.osta(HINTA)
            self.myytyja_lounaita = self.myytyja_lounaita + 1
