oncekiAsal = 2
simdikiAsal = 3
sonrakiAsal = 5
asalMi = True
for i in range(5,1000,1):
    asalMi = True
    for j in range(2,i,1):
        if i%j == 0:
            asalMi = False
    if asalMi == True:
        oncekiAsal = simdikiAsal
        simdikiAsal = sonrakiAsal
        sonrakiAsal = i
    if (oncekiAsal+sonrakiAsal)/2 == simdikiAsal and i == sonrakiAsal:
        print(simdikiAsal," dengeli bir asal sayidir.")