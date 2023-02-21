def funkcja():                                                     funkcja (bezargumentowa), która drukuje napis „czwartek”
	print(‘’czwartek”);
funkcja()

def funkcja(a): 					funkcja, która drukuje przeslany do niej napis (wartość)
	print(a);
funkcja(‘’czwartek”)


  
def funkcja(a): 					funkcja, która drukuje napis i zwraca jego dlugosc 
	print(a); 				        I sposób 
funkcja(‘’ala ma kota, kot ma ale”)
print(len(‘’ala ma kota, kot ma ale”))


def funkcja(a):
	print(a);                                                            II sposób
	return len(a)	
x=funkcja(‘’cos tam”)
print(‘’wynik,x”)
