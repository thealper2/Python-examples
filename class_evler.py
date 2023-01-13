class Daire:
    def __init__(self,odaSayisi,metreKare):
        self.__odaSayisi = odaSayisi
        self.__metreKare = metreKare
    def setOdasayisi(self,o1):
        self.__odaSayisi = o1
    def getOdasayisi(self):
        return self.__odaSayisi
    def setMetrekare(self,mk):
        self.__metreKare = mk
    def getMetrekare(self):
        return self.__metreKare
    def kiraHesapla(self):
        kira = self.getOdasayisi() * self.getMetrekare() * 10
        return kira
    def yazdir(self):
        print("Daire olusturuldu.")
        print("Dairenin oda sayisi:",self.getOdasayisi(),", metrekaresi:",self.getMetrekare())
        print("Kira: ",self.kiraHesapla())
class Apartman(Daire):
    def __init__(self,odaSayisi,metreKare,katSayisi,daireSayisi,ad):
        super().__init__(odaSayisi,metreKare)
        self.__katSayisi = katSayisi
        self.__daireSayisi = daireSayisi
        self.__ad = ad
    def setKatsayisi(self,kat):
        self.__katSayisi = kat
    def getKatsayisi(self):
        return self.__katSayisi
    def setDairesayisi(self,daire):
        self.__daireSayisi = daire
    def getDairesayisi(self):
        return self.__daireSayisi
    def setAd(self,adi):
        self.__ad = adi
    def getAd(self):
        return self.__ad
    def kiraHesapla(self):
        kira = self.getDairesayisi()*self.getKatsayisi()*self.getOdasayisi() * self.getMetrekare() * 10
        return kira
    def yazdir(self):
        print("Apartman olusturuldu.")
        print("Apartmanin kat sayisi:",self.getKatsayisi(),", metrekaresi:",self.getMetrekare())
        print("Kira: ",self.kiraHesapla())
class Site(Apartman):
    def __init__(self,odaSayisi,metreKare,katSayisi,daireSayisi,ad,binaSayisi,sitead):
        super().__init__(odaSayisi,metreKare,katSayisi,daireSayisi,ad)
        self.__binaSayisi = binaSayisi
        self.__sitead = sitead
    def setBinasayisi(self,bina):
        self.__binaSayisi = bina
    def getBinasayisi(self):
        return self.__binaSayisi
    def setSitead(self,site):
        self.__sitead = site
    def getSitead(self):
        return self.__sitead
    def kiraHesapla(self):
        kira = self.getBinasayisi()*self.getDairesayisi()*self.getKatsayisi()*self.getOdasayisi() * self.getMetrekare() * 10
        return kira
    def yazdir(self):
        print("Site olusturuldu.")
        print("Site bina sayisi:",self.getBinasayisi(),", metrekaresi:",self.getMetrekare())
        print("Kira: ",self.kiraHesapla())
d1 = Daire(3,100)
d1.kiraHesapla()
d1.yazdir()
print("\n")
a1 = Apartman(3,100,4,2,"lila")
a1.kiraHesapla()
a1.yazdir()
print("\n")
s1 = Site(3,100,4,2,"lila",5,"amatris konutlari")
s1.kiraHesapla()
s1.yazdir()