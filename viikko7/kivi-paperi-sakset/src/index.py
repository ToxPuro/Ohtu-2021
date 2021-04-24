from luo_kps import LuoKPS


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        kaksinpeli = LuoKPS.luo_kaksinpeli(vastaus)

        if(not kaksinpeli):
            break

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )    

        kaksinpeli.pelaa()




if __name__ == "__main__":
    main()
