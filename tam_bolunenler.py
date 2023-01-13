def tamBolunenler(x):
    bolum = 1
    print(x," sayisinin tam bolenleri:")
    while x>=bolum:
        if x%bolum == 0:
            print(bolum)
        bolum += 1
sayi = int(input("Bolenlerini bulmak istediginiz sayiyi girin: "))
tamBolunenler(sayi)