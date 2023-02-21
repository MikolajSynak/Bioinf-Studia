class Node(object):
    def __init__(self, nazwa):
        self.nazwa = nazwa
    def __str__(self):
        return(self.nazwa)
class Edge(object):
    def __init__(self, poczatek, koniec):
        self.poczatek = poczatek
        self.koniec = koniec
class Graf(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def dodajwierzcholek(self, node):
        if node in self.nodes:
            raise ValueError("Wierzcholek jest juz w grafie")
        else:
            self.nodes.append(node)
            self.edges[node]=[]
    def dodajKrawedz(self, edge):
        poczatek = edge.poczatek
        koniec = edge.koniec
        if not (poczatek in self.nodes and koniec in self.nodes):
            raise ValueError("masz pajaki pod skora ;)")
        else:
            
            self.edges[poczatek].append(koniec)
    def zwrocDzieci(self, node):
        return self.edges[node]
    def __str__(self):
        for imie1 in self.edges:
            for imie2 in self.edges[imie1]:
                print(str(imie1) + " ->", str(imie2))


Andrzej = Graf()


krystian = Node("Krystian")
Alojzy = Node("Alojzy")
Eugeniusz = Node("Eugeniusz")
Ebzdyberybencjusz = Node("Ebzdyberybencjusz")
Augustyn = Node("Augustyn")
Samolot = Node("Samolot")


Andzelina = Edge(krystian, Alojzy)
Paulina = Edge(Alojzy, Eugeniusz)
Elena = Edge(Eugeniusz, Ebzdyberybencjusz)
Eleonora = Edge(Ebzdyberybencjusz, Augustyn)
Marianna = Edge(Augustyn, Samolot)
Andrzejka = Edge(Samolot, krystian)


Andrzej.dodajwierzcholek(krystian)
Andrzej.dodajwierzcholek(Alojzy)
Andrzej.dodajwierzcholek(Eugeniusz)
Andrzej.dodajwierzcholek(Ebzdyberybencjusz)
Andrzej.dodajwierzcholek(Augustyn)
Andrzej.dodajwierzcholek(Samolot)

Andrzej.dodajKrawedz(Andzelina)
Andrzej.dodajKrawedz(Paulina)
Andrzej.dodajKrawedz(Elena)
Andrzej.dodajKrawedz(Eleonora)
Andrzej.dodajKrawedz(Marianna)
Andrzej.dodajKrawedz(Andrzejka)


print(Andrzej)


#Teraz szukamy Samolotu. Kto go zna?

kolejka = [krystian, Alojzy, Eugeniusz, Ebzdyberybencjusz, Augustyn, Samolot]
smietnik = []
for x in range(kolejka):
    x = 0
    if x != Samolot:
        kolejka.pop(0)
        smietnik.append(x)
        x = x + 1
    else:
        print("Samolot jest")
    if Samolot not in kolejka:
        print("Samolotu nie ma i nigdy nie bylo, zmien dilera")
