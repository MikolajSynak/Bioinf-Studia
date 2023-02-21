n = int(input("Podaj ilość liczb: "))
lista = []
for i in range(n) :
        x = float(input('Podaj liczby: '))
        lista.append(x)
print('wyrazy, które podałeś, to: ', lista)
zgoda = int(input('Kontynuować? Jeśli tak, wpisz "1": '))
if (zgoda == 1) :
    suma = 0
    for x in lista :
        suma = suma + x
    print("średnia cyfr, które podałeś, to: ", (suma/n))
else :
    print('zacznij od nowa')