import random
przegrana=0
remis=1
wygrana=2
oponent = input("wybierz jedno (papier, kamień, nożyce): ")
możliwości = ["papier", 'kamień', 'nożyce']
komp = random.choice(możliwości)
print("przeciwnik wybrał: ")
print(komp)
if (oponent=='kamień') and (komp=="kamień"):
    x = 1
    print("remis")
elif (oponent=='papier') and (komp=='papier'):
    x = 1
    print("remis")
elif (oponent=='nożyce') and (komp=='nożyce'):
    x = 1
    print("remis")
elif (oponent=="kamień") and (komp=="nożyce"):
    x = 2
    print("wygrana")
elif (oponent=="kamień") and (komp=="papier"):
    x = 0
    print("przegrana")
elif (oponent=="papier") and (komp=="nożyce"):
    x = 0
    print("przegrana")
elif (oponent=="papier") and (komp=='kamień'):
    x = 2
    print("wygrana")
elif (oponent=="nożyce") and (komp=="kamień"):
    x = 0
    print("przegrana")
elif (oponent=="nożyce") and (komp == "papier"):
    x = 2
    print("wygrana")
if (x==0):
    print("komp mówi że essa z tobą")
elif (x==1):
    print("komp twierdzi, że jesteś małpa")
elif (x==2):
    print("komp stwierdził, że oszukujesz")