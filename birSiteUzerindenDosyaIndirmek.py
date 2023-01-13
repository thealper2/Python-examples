import urllib.request

site_adres = input("Indirmek isteginiz dosyanin adresini girin: ")
dosya_adi = input("Dosyayi kaydetmek icin isim girin: ")

urllib.request.urlretrieve(site_adres, dosya_adi)
