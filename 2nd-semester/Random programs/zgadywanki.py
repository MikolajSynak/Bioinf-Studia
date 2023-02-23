#uzytkownik wpisuje liczbe i zgaduje tę wybraną przerz komputer
import random
komp = random.randint(1, 100)
oponent = 0
while(oponent != komp):
    oponent = int(input("Zgadnij, jaką liczbę wylosował komputer: "))
    if(oponent > komp):
        print("Nigdy tego nie zgadniesz jak będziesz podawał tak kolosalne liczby.")
    if(oponent < komp):
        print("Dałeś za mało. Nie doceniasz mojej mocy.")
print("Brawo!")