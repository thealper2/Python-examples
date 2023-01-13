def factoriyel(x):
    i=1
    fact=1
    while i<=x:
        fact = fact*i
        i += 1
    print(fact)
def factoriyelBas(x):
    a = 1
    while a<=x:
        print(a,"!=",factoriyel(a))
        a += 1
sayi = int(input("Faktoriyel sayisini girin:"))
factoriyel(sayi)
factoriyelBas(sayi)