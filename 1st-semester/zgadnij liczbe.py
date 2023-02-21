import random
a=random.randint(1,100)
p=0

while p!=a:
    p=int(input("zgadnij liczbe z przedzialu 1 do 100: "))
    if p>a:
        print("liczba jest mniejsza")
    elif p<a:
        print("liczba jest wieksza")
    else:
        print("prawidlowa odpowiedz")
