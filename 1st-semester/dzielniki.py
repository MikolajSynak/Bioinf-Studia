n=12
for k in range(1, n+1):
     if n % k == 0 :
         print(k, end=" , ")

"""
n=120
i=1
while i <= liczba:
    if n%i==0:
        print(i)
    i=i+1

def dzielniki(n):
    lista = []
    for i in range(1,n+1):
        if n%i==0:
            lista.append(i)
    return lista
print(dzielniki(1234))