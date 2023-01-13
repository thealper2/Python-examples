#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Derleme Programi")

print("""
Derleme Programina Hos Geldiniz.
""")

derle = raw_input("Program ismini girin: ")

py_compile.compile(derle)
