n=int(input(‘’podaj dla ilu liczb policzyć srednia:”))              SREDNIA (WYBÓR DLA ILU LICZB)
l=[]
for i in range(n):
	liczba=int(input(‘’podaj liczbe:”))
	l.append(liczba)
srednia=0
suma=0
for i in l:
	suma+=i
srednia=suma/n
print(f”srednia:{srednia}”)
