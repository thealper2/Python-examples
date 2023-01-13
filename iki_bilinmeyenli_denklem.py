import math
def kokleriHesapla(a,b,c):
    delta,x1,x2,x1re,x1sa,x2re,x2sa = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,
    print("Orn : ax2 + bx + c")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    delta = (b*b)-(4*a*c)
    kt = -b/a
    kc = c/a
    print("Kokler Toplami = ",kt)
    print("Kokler Carpimi = ",kc)
    if delta < 0:
        print("Reel kok yok.")
        delta = math.fabs(delta)
        x1re = -b/a
        x1sa = math.sqrt(delta)/(2*a)
        x2re = -b/a
        x2re = math.sqrt(delta)/(2*a)
        print("x1 = ",x1re," + i*",x1sa)
        print("x2 = ",x2re," - i*",x2sa)
    elif delta == 0:
        print("Simetrik iki kok var.")
        x1 = -b/(2*a)
        print("Kok = ",x1)
    elif delta > 0:
        print("Iki reel kok var.")
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 = ",x1)
        print("x2 = ",x2)
secim = 'e'
a1,b1,c1 = 0.0,0.0,0.0
while secim == 'e':
    kokleriHesapla(a1,b1,c1)
    secim = input("Devam etmek ister misiniz ? (e-Evet, h-Hayir)\n")
