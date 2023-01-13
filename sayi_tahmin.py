import random
sayi = random.randrange(1,101)
cevap = 'e'
while cevap == 'e':
    print("0,100 arasi bir sayi tahmin ediniz.")
    tahmin = int(input("Tahmininiz: "))
    while tahmin != sayi:
        if tahmin < sayi:
            print("Daha buyuk bir sayi tahmin edin")
        else:
            print("Daha kucuk bir sayi tahmin edin")
        tahmin = int(input("Tahmininiz: "))
    print("Tebrikler.Tuttugum sayi {} idi.".format(sayi))
    cevap = input('Tekrar oynayak mı ? (e-Evet, h-Sg)\n')
