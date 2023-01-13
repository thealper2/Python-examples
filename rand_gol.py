import random
gol = int(input("Galatasaray bu sezon kac gol atmistir ?\n"))
o1,o2,o3,o4,o5,o6 = 0,0,0,0,0,0
o1 = random.randrange(0,gol/2)
if o1 >= 0:
    print("Radamel Falcao : ",o1)
o2 = random.randrange(0,gol-o1)
if o2 >= 0:
    print("Younes Belhanda : ",o2)
o3 = random.randrange(0,gol-o1-o2)
if o3 >= 0:
    print("Ryan Babel : ",gol-o1-o2-o3)
o4 = random.randrange(0,gol-o3)
if o4 >= 0:
    print("Mostafa Muhammed : ",o4)
o5 = random.randrange(0,gol-o1-o2-o3-o4)
if o5 >= 0:
    print("DeAndre Yedlin : ",o5)
o6 = gol-o1-o2-o3-o4-o5
if o6 >= 0:
    print("Kerem Akturkoglu : ",o6)