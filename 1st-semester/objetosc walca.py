def objestosc(d,h):				funkcja, która na podstawie średnicy i wysokości oblicza objetosc walca
	v=(d/2)**2*3.14*h                      #3.14*d*d*h/4
	return v;
srednica=float(input(‘’podaj srednice”));
wysokość=float(input(‘’podaj wysokość));
v=objetosc(srednica,wysokosc)
print(‘’objetosc walca wynosi”,v)
