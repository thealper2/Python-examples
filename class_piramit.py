class piramit:
    def __init__(self,yuzeyUzunlugu,tabanUzunlugu,yukseklik):
        self.__yuzeyUzunlugu = yuzeyUzunlugu
        self.__tabanUzunlugu = tabanUzunlugu
        self.__yukseklik = yukseklik
    def setYuzeyUzunlugu(self,yu):
        self.__yuzeyUzunlugu = yu
    def getYuzeyUzunlugu(self):
        return self.__yuzeyUzunlugu
    def setTabanUzunlugu(self,tu):
        self.__tabanUzunlugu = tu
    def getTabanUzunlugu(self):
        return self.__tabanUzunlugu
    def setYukseklik(self,y):
        self.__yukseklik = y
    def getYukseklik(self):
        return self.__yukseklik
    def alan(self):
        alan = 0.0
        alan = self.__yukseklik * self.__tabanUzunlugu * self.__yuzeyUzunlugu
        return alan
    def hacim(self):
        hacim = 0.0
        hacim = (self.__yukseklik * self.__tabanUzunlugu * self.__yuzeyUzunlugu)/3
        return hacim
p = piramit(1,2,3)
p.alan()
p.hacim()
print("Alan : ",p.alan())
print("Hacim : ",p.hacim())