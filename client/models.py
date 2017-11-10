import datetime

class Tenperatura:

    def __init__(self, tenp):
        self.tenp = tenp
        self.garagardoa = 1
        # Garagardoa id bat da, ze garagardo egin den ikusteko, oraingoz beti 1

    def __str__(self):
        return "Tenperatura : "+str(self.tenp)+"ºC"
