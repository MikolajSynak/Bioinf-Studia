a=1.5                                                                   KAŻDA LICZBA PODNIESIONA DO POTEGI 1  
n=0                                                                        I
potega=1
for i in range(n):
        potega= potega*a
print("{}^{}={}".format(a,n,potega))
"""


def potega(a,n):                                                  II
	p=1
	for i in range(n):
		p=p*a
	return p
a=-1.5
n=3
print(‘’{}^{}={}’’.format(a,n,potega(a,n)))






"""




def potega(a,n):                                                                                 III
	p=1
	for i in range(n):
		p=p*a
	return p
#reukrencyjnie
def potegaRek(a,n):
    """a^0=1
    a^n=a*a^(n-1)"""
a=-2
n=3
print("{}^{}={}".format(a,n,potega(a,n)))
print("Rekurencyjnie:\n{}^{}={}".format(a,n,potegaRek(a,n)))

"""
def potega(a,n):        							IV
	p=1
	for i in range(n):
		p=p*a
	return p
#reukrencyjnie
def potegaRek(a,n):
    """a^0=1
    a^n=a*a^(n-1)"""
    if n==0:
        return 1
    else:
        return a*potegaRek(a,n-1)
a=-2
n=10
print("{}^{}={}".format(a,n,potega(a,n)))
print("Rekurencyjnie:\n{}^{}={}".format(a,n,potegaRek(a,n)))

