def megszamlalas():
    db = 0
    i = 10
    while i < 99:
        if i % 2 == 0:
            db += 1
        i += 1
    print(db)
def megszamlalasFor():
    db = 0
    for i in range(10,99):
        if i % 2 == 0:
            db += 1
    print(db)