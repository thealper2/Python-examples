def asalMi(x):
    for i in range(2,x,1):
        if x%i == 0:
            return False
        if x%i == 1:
            return True
sayac = 0
uslimit = int(input("Ust limit giriniz:"))
if uslimit < 2:
    print("En kucuk asal sayi 2'dir.Lutfen 2'den buyuk bir sayi giriniz.")
else:
    asalMi(uslimit)
    for i in range(2,uslimit+1,1):
        for j in range(1,i+1,1):
            if i%j == 0:
                sayac += 1
        if sayac == 2:
            print(i)
        sayac = 0