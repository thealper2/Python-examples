#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VULNERABILITY ANALYZER")
print("""
DENEME2 - VULNERABILITY ANALYZER
""")
hedefip = raw_input("Target ip: ")
os.system("nikto -h " +hedefip)