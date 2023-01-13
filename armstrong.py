def armstrong(sayi):
    x,y,z = 0,0,0
    for i in range(1,sayi,1):
        x = i/100
        y = (i%100)/10
        z = i%10
        if(x*x*x + y*y*y + z*z*z  == i):
            print(i," Armstrong sayisidir.")
    return sayi
sayi = int(input("Ust limit sayisi girin: "))
sayi2 = sayi
basamakSayisi = 0
while sayi > 0:
    sayi = sayi/10
    basamakSayisi += 1
print("Ust limit olan ",sayi2," sayisinin basamak sayisi : \n",basamakSayisi)
armstrong(sayi2)