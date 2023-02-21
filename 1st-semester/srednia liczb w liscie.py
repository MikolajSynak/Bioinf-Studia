def srednia(a):					funkcja, która oblicza srednia arytmetyczna liczb w liscie
	n=len(a)
	suma=0
	for i in range(n):
		suma=suma+a[i]
	suma=suma/n
	return suma
#1
a=[1,54,2826,46,-287,543]
x=srednia(a);                       #lub print(srednia(a))
print(x)

#2
suma=0
j=0
for i in a:
	srednia=srednia+i
	j+j+1
return suma/j

#3
Return sum(a)/len(a)
