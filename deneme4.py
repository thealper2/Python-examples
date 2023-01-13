#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet FIREWALLER")
print("""
DENEME4 - FIREWALL SCANNER
""")
w = raw_input("Target website adress: ")
os.system("wafw00f " +w)