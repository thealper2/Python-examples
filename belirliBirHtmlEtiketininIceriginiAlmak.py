import urllib.request
import re

address = input("Site adresi: ")
html = urllib.request.urlopen(address)
html = html.read()
html = str(html)
etiket = "<title>(.*?)</title>"
kontrol = re.search(etiket, html)
if kontrol:
	etiket = kontrol.group(0)
	print("Etiket: " + etiket)
	icerik = kontrol.group(1)
	print("Icerik: " + icerik)
else:
	print("Etiket yok.")
