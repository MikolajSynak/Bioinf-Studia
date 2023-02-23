x = int(input("Podaj liczbę - "))
y = int(input("Podaj liczbę - "))

def iloczyn(x, y):
    if (y == 1):
        return x
    else:
        return iloczyn(x, y-1) + x


print(iloczyn(x, y))