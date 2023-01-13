import math
class Sekil:
    def __init__(self,birim,sekilturu):
        self.__birim = birim
        self.__sekilturu = sekilturu
    def setBirim(self,br):
        self.__birim = br
    def getBirim(self):
        return self.__birim
    def setSekilturu(self,tur):
        self.__sekilturu = tur
    def getSekilturu(self):
        return self.__sekilturu
class Ucgen(Sekil):
    def __init__(self,birim,sekilturu,yukseklik,taban):
        super().__init__(birim,sekilturu)
        self.__yukseklik = yukseklik
        self.__taban = taban
    def setYukseklik(self,y):
        self.__yukseklik = y
    def getYukseklik(self):
        return self.__yukseklik
    def setTaban(self,t):
        self.__taban = t
    def getTaban(self):
        return  self.__taban
    def Alan(self):
        alan = (self.__yukseklik * self.__taban)/2
        return alan
class Dortgen(Sekil):
    def __init__(self,birim,sekilturu,en,boy):
        super().__init__(birim,sekilturu)
        self.__en = en
        self.__boy = boy
    def setEn(self,e):
        self.__en = e
    def getEn(self):
        return self.__en
    def setBoy(self,b):
        self.__boy = b
    def getBoy(self):
        return  self.__boy
    def Alan(self):
        alan = (self.__en * self.__boy)
        return alan
class Daire(Sekil):
    def __init__(self,birim,sekilturu,yaricap):
        super().__init__(birim,sekilturu)
        self.__yaricap = yaricap
    def setYaricap(self,r):
        self.__yaricap = r
    def getYaricap(self):
        return self.__yaricap
    def Alan(self):
        alan = (self.__yaricap * self.__yaricap * math.pi)
        return alan
class Kare(Sekil):
    def __init__(self,birim,sekilturu,kenar):
        super().__init__(birim,sekilturu)
        self.__kenar = kenar
    def setKenar(self,k):
        self.__kenar = k
    def getKenar(self):
        return self.__kenar
    def Alan(self):
        alan = (self.__kenar * self.__kenar)
        return alan
s1 = Ucgen("cm2","Ucgen",3,4)
s2 = Dortgen("cm2","Dikdortgen",7,8)
s3 = Daire("cm2","Daire",3)
s4 = Kare("cm2","Kare",5)
print(s1.getSekilturu()," cismi ",s1.Alan(),s1.getBirim()," alana sahiptir.")
print(s2.getSekilturu()," cismi ",s2.Alan(),s2.getBirim()," alana sahiptir.")
print(s3.getSekilturu()," cismi ",s3.Alan(),s3.getBirim()," alana sahiptir.")
print(s4.getSekilturu()," cismi ",s4.Alan(),s4.getBirim()," alana sahiptir.")

