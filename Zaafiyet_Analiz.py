#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zaafiyet Analizi")
print("""
Zaafiyet Analizi Programina Hos Geldiniz.
""")

hedefip = raw_input("Hedef IP Girin: ")

os.system("nikto -h " + hedefip)
