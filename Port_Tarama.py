#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figled")
os.system("clear")
os.system("figlet PORT TARAMA")
print(""" Port Tarama Programina Hos Geldiniz.

1) Hizli Tarama
2) Servis ve Versiyon Bilgisi
3) Isletim Sistemi Bilgis

""")

islemno = raw_input("Islem numarasini girin: ")

if(islemno == "1"):
	hedefip = raw_input("Hedef IP girin: ")
	os.system("nmap " + hedefip)
elif(islemno == "2"):
	hedefip = raw_input("Hedef IP girin: ")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno == "3"):
	hedefip = raw_input("Hedef IP girin: ")
	os.system("nmap -O "  + hedefip)
else:
	print("Hatali secim yaptiniz.Program Kapatiliyor.")
