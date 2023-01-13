#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MACHANGE")

print("""
DENEME14 - MAC CHANGER
1) MAC Random
2) MAC Manual
3) MAC Turn Back
""")

opno = raw_input("Choose one: ")
if opno == "1" :
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("MAC degistirildi")
elif opno == "2":
	macadr = raw_input("New MAC Adress: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadr + " eth0")
	os.system("ifconfig eth0 up")
	print("MAC degistirildi")
elif opno == "3":
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("MAC degistirildi")
else:
	print("")