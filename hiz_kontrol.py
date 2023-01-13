tur = input('Aracin turunu giriniz (o=Otomobil, t=Tir, k=Kamyon): ')
hiz = int(input("Aracin hizini giriniz : "))
if tur == 'o':
    print("Arac otomobildir.")
    if hiz > 82:
        print("Arac cezalidir.")
    else:
        print("Arac kurallara uygundur.")
elif tur == 't':
    print("Arac tirdir.")
    if hiz > 70:
        print("Arac cezalidir.")
    else:
        print("Arac kurallara uygundur.")
elif tur == 'k':
    print("Arac kamyondur.")
    if hiz > 50:
        print("Arac cezalidir.")
    else:
        print("Arac kurallara uygundur.")
else:
    print("Arac turunu veya hizini yanlis girdinizki.")