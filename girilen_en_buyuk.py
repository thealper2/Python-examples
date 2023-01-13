def enbuyuksayi(n):
    enbuyuk = 0
    for i in range(0,n,1):
        sayi = int(input())
        if sayi > enbuyuk:
            enbuyuk = sayi
    return enbuyuk
n = int(input("Kac sayi gireceksiniz: "))
print("Girilen sayilarin en buyugu: ",enbuyuksayi(n))