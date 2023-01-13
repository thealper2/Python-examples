#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Worldlist Olustur")
print("""
Wordlist Olusturma Programina Hos Geldiniz.
""")

minimumkarakter = raw_input("Minimum karakter sayisini girin: ")
maksimumkarakter = raW_input("Maksimum karakter sayisini girin: ")
karakter = raw_input("Istediginiz karakterleri girin: ")
kayityeri = raw_input("Kaydedilecek yeri girin: ")

os.system("crunch " + minimumkarakter + " " + maksimumkarakter + " " + karakter + " -D " + kayityeri)

print("Islem basariyla tamamlandi.") 
