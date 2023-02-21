dane=[3.14,99,-74,92,47,4,2,0]
szukany=-74
znaleziono=false
for x in sorter(dane):
	if x==szukany:
		znaleziono=true
		break
	if x>=szukany:
		break
if znaleziono:
	print(‘’liczba {} jest na liście’’.format(szukany))
else:
	print(‘’liczby {} nie ma na liście’’.format(szukany))
