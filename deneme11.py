#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS SCAN")
print("""
DENEME11 - WORDPRESS SCAN
1) Fast Scan
2) Extention Scan
3) Theme Scan
4) Adminastator Username Scan
""")
opno = raw_input("Choose one: ")
if(opno == "1"):
	adr = raw_input("Website adress: ")
	os.system("wpscan --url " +adr)
elif(opno == "2"):
	adr = raw_input("Website adress: ")
	os.system("wpscan --url " +adr +" --enumerate p")
elif(opno == "3"):
	adr = raw_input("Website adress: ")
	os.system("wpscan --url " +adr +" --enumerate t")
elif(opno == "4"):
	adr = raw_input("Website adress: ")
	os.system("wpscan --url " +adr +" --enumerate u")
else:
	print("")