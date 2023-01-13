#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BRUTE GUY")
print("""
DENEME5 - Brute Force Tool
1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) ROP
7) SIP
8) Redis
9) VNC
10) PostgreSQL
11) MySQL
""")
opno = raw_input("Choose One: ")
tip = raw_input("Target Ip: ")
usrpath = raw_input("Username Path: ")
passw = raw_input("Password Path: ")
if(opno == "1"):
	os.system("nrack -p 21 -u " +usrpath " -p " +passw " " +tip)
elif(opno == "2"):
	os.system("nrack -p 22 -u " +usrpath " -p " +passw " " +tip)
else:
	print("m0b")