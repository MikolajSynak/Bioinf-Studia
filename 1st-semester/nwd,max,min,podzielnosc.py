a=iny(input(‘’podaj wartość a:’’))                                             NAJWIĘKSZY WSPÓLNY DZIELNIK
b=int(input(‘’podaj wartość b:’’))
while a!=b
	if a>b:
		a=a-b
	else:
		b=b-a
print(‘’największy wspólny dzielnik wynosi’’, b)


n=123456
while n!=0:
	print(n%10)
	n=n//10


dane=[3.14,99,-74,92,47,4,2,0,-273]
minimum=maksimum=dane[0]
for x in dane:
	if x<minimum:
		minimum=x
	if x>maksimum:
		maksimum=x
print(minimum, maksimum)
