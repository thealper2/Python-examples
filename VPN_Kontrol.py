#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN Kontrol")
print("""
VPN Kontrol Programina Hos Geldiniz.
""")

hedefip = raw_input("Hedef IP Girin: ")

os.system("ike-scan " + hedefip)
