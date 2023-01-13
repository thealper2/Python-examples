ad = input("Ad girin: ")
print("Merhaba " + ad + " beraber adam asmaca oynayalim.")
gizli_kelime = "galatasaray"
tahmin = ""
can = 12
while can > 0:
    kalan = 0
    for karakter in gizli_kelime:
        if karakter in tahmin:
            print(karakter)
        else:
            print ("-")
            kalan += 1
    if kalan == 0:
        print("Tebrikler! Kazandiniz")
        break
    tahmini = input("Tahmin et: ")
    tahmin += tahmini
    if tahmini not in gizli_kelime:
        can -= 1
        print("Yanlis")
        print(f"{can} hakkiniz kaldi.")
    if can == 0:
        print("Kaybettiniz")
