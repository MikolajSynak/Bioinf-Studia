#Napisz program, który:
#1. Prosi użytkownika o podanie liczby i bazy (od 1 do 20), w której ta liczba ma być zapisana.
#2. Zamienia tę liczbę na bazę wpisaną przez użytkownika
#3. Wyświetla tę liczbę w nowej bazie.
#Dobra, lecimy.

x = int(input("Podaj liczbę z której nie jesteś zadowolony w systemie dziesiętnym - "))
y = int(input("Podaj system w który chcesz zamienić powyższą liczbę (w postaci cyfry od 1 do 20) - "))

if y >= 21:
    print("Od 1 do 20 baranie. Teraz resetuj program.")
if y <= 0:
    y = int(input("Od 1 do 20 baranie. Za karę resetujesz program. Napisz tu wiadomość do developera i resetuj - "))

baza = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
lista = []
lista2 = []
for i in range(0, y):
    lista.append(baza[i])
z = 1
while (x > 0):
    z = x % y
    lista2.append(lista[z])
    z = x//y
    x = z
lista2.reverse()
print(lista2)

