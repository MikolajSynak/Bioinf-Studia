lista=[2,6,37,47,28,49,9,17]                                       SPRAWDZANIE CZY LICZBA JEST NA LIŚCIE
print(47 in lista) 

"""                                                               I SPOSÓB
	
lista=[2,6,37,47,28,49,9,17]                                       II SPOSÓB
szukany=9
for x in lista:
	if szukany==x:
		print(‘’liczba {} jest na liście’’.format(szukany))
		break
else:
	print(‘’liczba {} nie jest na liście’’.format(szukany))

"""
lista=[2,47,6,37,47,28,49,9,17,47]                                               ILE RAZY DANA LICZBA WYSTĄPIŁA       
szukany=47
n=0
for x in lista:
	if szukany==x:
		n=n+1
print(‘’liczba {} wystąpiła {} razy’’.format(szukany, n))
