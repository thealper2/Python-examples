class tarih:
    def __init__(self,gun,ay,yil):
        self.__gun = gun
        self.__ay = ay
        self.__yil = yil
    def setGun(self,g):
        if g < 0 or g > 31:
            print("Hatali gun bilgisi girdiniz.")
        else:
            self.__gun = g
    def getGun(self):
        return self.__gun
    def setAy(self,a):
        if a < 0 or a > 12:
            print("Hatali ay bilgisi girdiniz.")
        else:
            self.__ay = a
    def getAy(self):
        return self.__ay
    def setYil(self,y):
        if y < 0:
            print("Hatali yil bilgisi girdiniz.")
        else:
            self.__yil = y
    def getYil(self):
        return self.__yil
t = tarih(12,10,2020)
print("Tarih: ",t.getGun(),"/",t.getAy(),"/",t.getYil())