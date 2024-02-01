def maximum():
    VEGE = 0
    min = 247483647
    db = 0
    while (szam := int(input("Szam"))) != VEGE:
        if szam < min:
            min = szam
        db += 1
    print(f"{min}")
