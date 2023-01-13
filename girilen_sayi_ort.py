def ortalama(n):
    toplam = 0.0
    for i in range(0,n,1):
        sayi = int(input())
        toplam += sayi
    return toplam/n
n = int(input("Kac sayi gireceksiniz ?\n"))
print("Girilen sayilarin ortalamasi : ",ortalama(n))