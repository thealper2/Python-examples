#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""
Wordpress Tarama Programina Hos Geldiniz.

1) Hizli Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yonetici Kullanici Adi Tarama
""")

islemno = raw_input("Islem numarasini girin: ")

if(islemno == "1"):
	site = raw_input("Site adresi girin: ")
	os.system("wpscan --url " + site)
elif(islemno == "2"):
	site = raw_input("Site adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate p")
elif(islemno == "3"):
	site = raw_input("Site adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate t")
elif(islemno == "4"):
	site = raw_input("Site adresi girin: ")
	os.system("wpscan --url " + site + " --enumerate u")
else:
	print("Hatali secim yaptiniz. Program kapatiliyor.")
