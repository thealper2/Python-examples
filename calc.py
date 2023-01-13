import math
sayi1,sayi2,radyan,derece,sonuc = 0.0,0.0,0.0,0.0,0.0
print("|--------------------------------------------------------------------|")
print("|					1-)Toplama islemi icin 1 giriniz.                |")
print("|					2-)Cikarma islemi icin 2 giriniz.			 	 |")
print("|					3-)Carpma islemi icin 3 giriniz.                 |")
print("|					4-)Bolme islemi icin 4 giriniz.                  |")
print("|					5-)Ustel islemi icin 5 giriniz.                  |")
print("|					6-)Logaritmik islemi icin 6 giriniz.             |")
print("|					7-)ln islemi icin 7 giriniz.                     |")
print("|					8-)Koklu islemi icin 8 giriniz.                  |")
print("|					9-)Trigonometrik islemi icin 9 giriniz.          |")
print("|--------------------------------------------------------------------|")
trch = int(input("Secim yapiniz: "))
while trch >= 1 or trch <= 9:
    if trch == 1:
        print("Toplama islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        sayi2 = int(input(""))
        print("Sonuc = ",sayi1," + ",sayi2," = ",sayi1+sayi2)
        break
    elif trch == 2:
        print("Cikarma islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        sayi2 = int(input(""))
        print("Sonuc = ", sayi1, " - ", sayi2, " = ", sayi1-sayi2)
        break
    elif trch == 3:
        print("Carpma islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        sayi2 = int(input(""))
        print("Sonuc = ", sayi1, " * ", sayi2, " = ", sayi1*sayi2)
        break
    elif trch == 4:
        print("Bolme islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        sayi2 = int(input(""))
        print("Sonuc = ", sayi1, " / ", sayi2, " = ", sayi1/sayi2)
        break
    elif trch == 5:
        print("Ustel islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input("Taban: "))
        sayi2 = int(input("Us: "))
        print("Sonuc = ", sayi1, " ^ ", sayi2, " = ",math.pow(sayi1,sayi2))
        break
    elif trch == 6:
        print("Logaritma islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        print("Sonuc = ",math.log10(sayi1))
        break
    elif trch == 7:
        print("ln islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        sayi2 = int(input(""))
        print("Sonuc = ",math.log(sayi1,sayi2))
        break
    elif trch == 8:
        print("Karekok islemi secildi,sayilari giriniz:\n")
        sayi1 = int(input(""))
        print("Sonuc = ",math.sqrt(sayi1))
        break
    elif trch == 9:
        print("Trigonometrik islem secildi yapmak istediginiz islemi secin: ")
        print("********************************")
        print("*			1.Sinus             *")
        print("*			2.Arcsin            *")
        print("*			3.Cosec             *")
        print("*			4.Arccosec          *")
        print("*			5.Cosinus           *")
        print("*			6.Arccos            *")
        print("*			7.Sec               *")
        print("*			8.Arcsec            *")
        print("*			9.Tanjant           *")
        print("*			10.Arctan           *")
        print("*			11.Cotanjant		*")
        print("*			12.Arccot           *")
        print("********************************")
        sec = int(input("Secim : "))
        if sec == 1:
            sayi1 = int(input("Sinus hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi) / 180
            print("Sayinin radyan degeri: ",radyan)
            print("Sin: ",math.sin(radyan))
            break
        elif sec == 2:
            sayi1 = int(input("Arcsin hesaplamak istediginiz sayiyi girin: "))
            print("Sayinin radyan degeri: ",math.asin(sayi1))
            print("Arcsin: ", math.asin(sayi1)*57.2957795)
            break
        elif sec == 3:
            sayi1 = int(input("Cosec hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi) / 180
            print("Radyan cinsinden degeri: ", (1/math.sin(radyan))*57.2957795)
            break
        elif sec == 4:
            sayi1 = int(input("Arccosec hesaplamak istediginiz sayiyi girin: "))
            radyan = math.asin(1/sayi1)
            print("Radyan cinsinden degeri: ", radyan*57.2957795)
            break
        elif sec == 5:
            sayi1 = int(input("Cosinus hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi) / 180
            print("Sayinin radyan degeri: ", radyan)
            print("Cos: ", math.cos(radyan))
            break
        elif sec == 6:
            sayi1 = int(input("Arccos hesaplamak istediginiz sayiyi girin: "))
            print("Sayinin radyan degeri: ", math.acos(sayi1))
            print("Arcsin: ", math.acos(sayi1) * 57.2957795)
            break
        elif sec == 7:
            sayi1 = int(input("Sec hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi) / 180
            print("Radyan cinsinden degeri: ", 1/math.cos(radyan))
            print("Sec: ",(1/math.cos(radyan))*57.2957795)
            break
        elif sec == 8:
            sayi1 = int(input("Arcsec hesaplamak istediginiz sayiyi girin: "))
            radyan = math.acos(1/sayi1)
            print("Radyan cinsinden degeri: ",radyan)
            print("Arcsec: ",(radyan)*57.2957795)
            break
        elif sec == 9:
            sayi1 = int(input("Tanjant hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi)/180
            print("Radyan cinsinden degeri: ",radyan)
            print("Tan: ",math.tan(radyan))
            break
        elif sec == 10:
            sayi1 = int(input("Arctan hesaplamak istediginiz sayiyi girin: "))
            radyan = math.atan(radyan)
            print("Radyan cinsinden degeri: ", radyan)
            print("Arctan: ",(radyan)*57.2957795)
            break
        elif sec == 11:
            sayi1 = int(input("Cot hesaplamak istediginiz sayiyi girin: "))
            radyan = (sayi1 * math.pi) / 180
            print("Radyan cinsinden degeri: ", radyan)
            print("Cot: ", math.cos(radyan)/math.sin(radyan))
            break
        elif sec == 12:
            sayi1 = int(input("Arccot hesaplamak istediginiz sayiyi girin: "))
            radyan = math.atan(1/sayi1)
            print("Radyan cinsinden degeri: ", radyan)
            print("Arccot: ",(radyan)*57.2957795)
            break
        else:
            print("Hatali secim yaptiniz.")
            break
    else:
        print("Hatali secim yaptiniz.")
        break