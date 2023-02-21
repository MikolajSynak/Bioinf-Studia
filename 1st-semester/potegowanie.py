a=1.5
n=14

potega=1
for i in range(n):
    potega= potega * a
print("{} ^ {} = {}" .format(a,n,potega))
"""
"""
def potega(a, n):
    p = 1
    for i in range(n):
         p= p * a
    return p
    "a^n= a * a^(n-1) "
a=-1.5
n=3
print("{} ^ {} = {}" .format(a, n,potega(a, n)))