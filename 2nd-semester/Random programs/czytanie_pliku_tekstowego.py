# napisz program, ktry czyta plik tekstowy i wypisuje linie z niego
f = open("dane.txt")

liczby = f.readlines()
print("Twoje liczby to ", liczby)
liczby = [int(x) for x in f.readlines()]
def sredniaarytmetyczna():
    srednia = sum(liczby) / len(liczby)

sredniaarytmetyczna()
