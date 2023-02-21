import random
x=0
for p in range(1,11):
    a=random.randint(1,10)
    b=random.randint(1,10)
    wynik=a*b

    wynik=int(input("pomnoz liczbe {} przez {} " .format(a,b)))
    if wynik==a*b:
            print("prawidlowa odpowiedz")
            x=x+1
    else:
            print("zla odpowiedz, poprawna odpowiedz to {}" .format(a*b))
if(x==10):
    print("ocena 6")
elif(x==9) or (x==8):
    print("ocena 5")
elif (x==7) or (x==6):
    print("ocena 4")
elif (x==5) or (x==4):
    print("ocena 3")
elif (x==3):
    print ("ocena 2")
else:
    print("ocena 1")
