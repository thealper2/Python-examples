import urllib.request

site_adresi = input("Hangi siteye girmek istiyorsunuz ? : ")
html = urllib.request.urlopen(site_adresi)
print(site_adresi + ' adresinin kaynak kodu: \n')
print(html.read())
