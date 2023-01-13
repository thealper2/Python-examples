#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPNER")
print("""
DENEME13 - VPN CONTROLLER
""")
tip = raw_input("Target IP: ")
os.system("ike-scan "+tip)