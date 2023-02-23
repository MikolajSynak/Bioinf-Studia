n = int(input("Podaj liczbę - "))

def silnia(n):
    if n==0:
        return 1
    else:
        return n*silnia(n-1)

print(silnia(n))