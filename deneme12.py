#!/usr/bin/env python
import os
import py_compile
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet COMPILER")
print("""
DENEME12 - COMPILER
""")
comp = raw_input("File Name: ")
py_compile.compile(comp)