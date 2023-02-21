l=[3,6,’a’,73]                     WYPISANIE CAŁEJ LISTY, WSZYSTKICH ZNAKÓW PO KOLEI
for a in l:		  I SPOSÓB
	print(a)


l=[3,6,’a’,73]                     II SPOSÓB
for a in range(0,len(l)):
	print(l[a])


a=[3,6,’a’,73]                     PODANIE CAŁEJ LISTY I PÓŹNIEJ KAŻDY ELEMENT PO KOLEI ALE OD KOŃCA
print(a)
i=len(a)-1
while i>=0:
	print(a[i])
	i-=1

l=[]						
for i in range(10):
	liczba=float(input(‘’podaj liczbe:”))
	l.append(liczba)
print(l)
