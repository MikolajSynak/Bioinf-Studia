while True:
        a=int(input("podaj wartosc a: "))
        if a>=1:
                break
while True:
        b=int(input("podaj wartosc b: "))
        if b>=1:
            break
while a!=b:
    if a>b:
        a=a-b
    else: 
        b=b-a
print("najwiekszy wspolny dzielnik wynosi:",b)