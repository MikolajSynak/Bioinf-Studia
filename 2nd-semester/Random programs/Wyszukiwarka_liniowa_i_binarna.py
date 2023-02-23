lista = ["Alfabet", "Barnaba", "Clarendon", "Dobromir", "Korzeń", "Koza", "Lawenda", "Lorem Ipsum", "Morze", "Zygzak", "Zzz", "Bubr", "Rzubr"]
x = str(input("Podaj szukane słowo z listy - "))
y = len(lista)
def google(z):
    for i in range(y):
        if x == lista[i]:
            return True
    return False
print(google(x))
def binoogle(x, lista):
    if len(lista)==0:
        return False
    srodek = len(lista)//2

    if x == lista[srodek]:
        return True
    elif x < lista[srodek]:
        #przeszukaj pierwszą połowę listy
        return binoogle(x, lista[:srodek])
    else:
        return binoogle(x, lista[srodek +1:]) #przeszukaj drugą połowę listy
print(binoogle(x, lista))