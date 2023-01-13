import requests
dosya = open("fuzzing.txt","r")
icerik = dosya.read()
dosya.close()
header = {"buraya burp suite programindaki cooki kismi kopyalanacak"}
for i in icerik.split("\n"):
    print(i)
    url = "ip_address" + str(i)
    sonuc = requests.get(url = url,headers = header)
    if "200" in str(sonuc.status_code):
        print("Dosya veya dizin var : ",i)
    else:
        print("Dosya veya dizin yok : ",i)