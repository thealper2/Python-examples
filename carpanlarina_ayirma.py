sayi = int(input("Bir sayi giriniz : "))
carpan = 2
while sayi > 1:
    while sayi%carpan == 2:
        print(carpan)
        sayi /= carpan
    carpan += 1
