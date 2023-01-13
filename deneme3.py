#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet EXPLOIT SCANNER")
print("""
DENEME3 - EXPLOIT SCANNER
""")
key = raw_input("Search: ")
os.system("searchloit " +key)
wish = raw_input("Search again (y/n) : ")
if(wish == "y"):
	os.system("python deneme3.py")
else:
	print("designed by m0b")