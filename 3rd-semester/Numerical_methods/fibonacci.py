
def Fiboniarz(n):
    if n < 0:
        print("podaj większą od 0")

    elif n == 0:
        return 0


    elif n == 1 or n == 2:
        return 1

    else:
        return Fiboniarz(n - 1) + Fiboniarz(n - 2)

x = int(input("Podaj liczbę: "))
y = Fiboniarz(x)
if x < 1000:
    print("twoj wynik ciągu to: {}".format(y))
else:
    print("podaj moze mniejszą liczbę to zobaczymy;)")