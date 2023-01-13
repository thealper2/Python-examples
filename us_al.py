def usAl(taban,us):
    if us == 0:
        return 1
    elif us < 0:
        return (1/taban)*usAl((1/taban),(-us-1))
    return taban*usAl(taban,us-1)
taban = int(input("Taban giriniz: "))
us = int(input("Us giriniz: "))
print(usAl(taban,us))
