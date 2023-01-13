sayi = 0
sayac = 1
secim = 'e'
while secim == 'e':
    sayi = int(input())
    if sayi > 2:
        while sayac < sayi-1:
            sayac += 1
            if sayi%sayac == 0:
                print("Asal degildir.")
                break
            elif sayi%sayac == 1:
                print("Asaldir.")
    secim = input('Devam ? (e-Evet, h-Hayir)\n')
    sayac = 1