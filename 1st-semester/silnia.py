n=int(input(‘’podaj liczbe:”))                                                     OBLICZANIE SILNII WYBRANEJ ILOSCI LICZB
silnia=1 
i=1
while i<=n:
	print(‘’mnoze przez wartość liczby zmiennej”,i)
	silnia*=i
	i+=1
print(silnia)
silnia=1
for i in range(1,n-1):
	silnia+=i
print(silnia)
