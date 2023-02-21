dane=[3.14,99,-74,92,47,4,2,0,-273]
minimum=dane[0]
for x in dane:
	if x<minimum:
		minimum=x
print(minimum)
def NWD(a,b):
	if a==0: return b
	if b==0: return a 
	while a!=b:
		if a>b:
			a=a-b
		else:
			b=b-a
	return a
a=60
b=36
wynik=NWD(a,b)
print(‘’NWD({},{})={}’’.format(a,b,wynik))
