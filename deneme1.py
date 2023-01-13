#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT SCAN")
print("""
DENEME1 - PORT SCANNER
1) Fast Scan
2) Info
3) System Info
""")
islemno = raw_input("Choose one: ")
if(islemno == "1"):
	hedefip = raw_input("Target ip: ")
	os.system("nmap " +hedefip)
elif(islemno == "2"):
	hedefip = raw_input("Target ip: ")
	os.system("nmap -sS -sV " +hedefip)
elif(islemno == "3"):
	hedefip = raw_input("Target ip: ")
	os.system = ("nmap -0 " +hedefip)
else:
	print("invalid type")