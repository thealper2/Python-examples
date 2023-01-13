def enkucuksayi(n):
    enkucuk = 99999
    for i in range(0,n,1):
        sayi = int(input())
        if sayi < enkucuk:
            enkucuk = sayi
    return enkucuk
n = int(input("Kac sayi gireceksiniz: "))
print("Girilen sayilarin en kucugu: ",enkucuksayi(n))