n = int(input("Podaj liczbę - "))
z = int(input("Podaj liczbę - "))
def potegaRek(n, z) :
    if z == 0:
        return 1
    else:
        return n * potegaRek(n, z-1)

print(potegaRek(n, z))