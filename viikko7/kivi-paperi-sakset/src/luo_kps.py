from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps_tekoaly import KPSTekoaly

class LuoKPS:
  @staticmethod
  def luo_kaksinpeli(valinta):
    if valinta.endswith("a"):
      return KPSPelaajaVsPelaaja()
    elif valinta.endswith("b"):
      return KPSTekoaly()
    elif valinta.endswith("c"):
      return KPSParempiTekoaly()
    else:
      return False