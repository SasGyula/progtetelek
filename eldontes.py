import math


def eldontes():
    n = int(input("N= "))
    prim = True
    #print(math.sqrt(n))
    if n < 2:
        prim = False
    else:
        i = 2
        while i <= math.sqrt(n) and n % i != 0:
            i = i + 1
        prim = i > math.sqrt(n)
    if prim:
        print(f"{n} Prím!")
    else:
        print(f"{n} Nem prím!")