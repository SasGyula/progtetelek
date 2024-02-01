def oszto(szam):
    lista = []
    for i in range(2, szam+1, 1):
        if szam % i == 0 and i != szam:
            lista.append(i)
    return lista
def kiir(lista):
    print(f"{lista}")

