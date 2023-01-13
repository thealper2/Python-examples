#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Firewall Tespit")
print("""
Firewall Tespit Programina Hos Geldiniz.
""")

site = raw_input("Site adresini girin: ")
os.system("wafw00f " + site)
