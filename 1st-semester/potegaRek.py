def potegaRek(a, n):
    a n= a * a^(n-1)
    for i in range(n):
        a*n= a * a^(n-1)
    return a*n
a=-2
n=3
print("rekurencyjnie: \n{} ^ {} = {}" .format(a, n, potegaRek(a, n)))
"""
"""
n=12
for k in range(1, n+1):
     if n % k == 0 :
         print(k, end=" , ")