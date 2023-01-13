ogr = []
gecenler = 0
gecemeyenler = 0
toplam = 0
for i in range(0,10,1):
    nott = int(input("Ogrenci notu giriniz: "))
    toplam += nott
    ogr.append(nott)
print("-----Ogrenci Notlari-----")
for i in range(0,10,1):
    print(i+1,". ogrenci : ",ogr[i])
for i in range(0,10,1):
    if ogr[i] >= 50:
        gecenler += 1
    else:
        gecemeyenler += 1
ortalama = toplam/10
print("Gecen ogrenci sayisi: ",gecenler)
print("Kalan ogrenci sayisi: ",gecemeyenler)
print("Toplam not: ",toplam)
print("Sinif ortalamasi: ",ortalama)