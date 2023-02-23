x = int(input("Podaj liczbę - "))
y = int(input("Podaj liczbę - "))

def suma(x, y):
    if (y == 0):
        return x
    else:
        return suma(x, y-1) + 1


print(suma(x, y))