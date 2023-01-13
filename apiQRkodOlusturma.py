import urllib.parse
import urllib.request

try:
	size = input("Resim boyutu (Orn: 150): ")
	veri = input("Icerik: ")
	
	veriler = {
		'size' : size + "x" + size,
		'data' : veri
	}
	
	parametreler = urllib.parse.urlencode(veriler)
	api_link = "https://api.qrserver.com/v1/create-qr-code/?" + parametreler
	urllib.request.urlretrieve(api_link, "kare_kod.png")
	
	print("Kare kod basariyla olusturuldu. kare_kod.png olarak kaydedildi.")
	print("\n")
except:
	print("Beklenmeyen bir hata olustur.")
