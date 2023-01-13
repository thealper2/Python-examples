def asal(n):
    for i in range(2,n,1):
        if n%i == 0:
            return False
    return True
sayi = int(input("Sayi gir: "))
print("Asallar :")
for i in range(2,sayi+1,1):
    if asal(i):
        print(i)