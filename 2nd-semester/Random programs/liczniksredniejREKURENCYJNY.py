a = [1,2,3,5,6]
def srednia(a):
    n=len(a)
    suma = 0
    for i in range(n):
        suma = suma + a[i]
    suma = suma / n
    return suma
x = srednia(a)
print("wynik to", x)