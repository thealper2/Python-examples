#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC Degistirme")
print("""
MAC Adres Degistirme Programina Hos Geldiniz.

1) MAC Adresi Random Belirle
2) MAC Adresi Elle Belirle
3) MAC Adresi Orijinale Dondur
""")

islemno = raw_input("Islem no girin: ")

if(islemno == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[93mYeni MAC Adresi Random Belirlendi.")
if(islemno == "2"):
	macadres = raw_input("Yeni MAC Adresi girin: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0)
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresi Elle Belirlendi.")
if(islemno == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adresi Orijinale Donduruldu.")
