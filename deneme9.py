#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WLIST")
print("""
DENEME9 - WLIST MAKER
""")
min = raw_input("Minimum char: ")
max = raw_input("Maximum char: ")
char = raw_input("Char: ")
path = raw_input("Path: ")
os.system("crunch " + min + " " + max + " " + char + " -o " +path)
print("wordlisted.")