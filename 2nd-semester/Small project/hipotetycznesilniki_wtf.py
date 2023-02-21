import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# wpisuję dane. Lista "x" odpowiada datom a "y" wydajności wczesnych silników parowych w procentach.
x = np.array([1718, 1767, 1774, 1775, 1792, 1816, 1828, 1834, 1878, 1906, 2000]).reshape((-1, 1))
# Dlaczego użyłem ".reshape((-1, 1)"? Bo x musi być dwuwymiarowy...
# tak wynika z opisu tej funkcji na necie, nie pytaj bo sam nie łapię xd
y = np.array([0.5, 0.8, 1.4, 2.7, 4.5, 7.5, 12.0, 17.0, 17.2, 23.0, 34.986133699909686])

# To jest chyba niepotrzebne ale jebac
model = LinearRegression()
model.fit(x, y)
r_kw = model.score(x, y)
print('nasz współczynnik determinacji w R2:', r_kw)

# Współczynnik w R2 wyszedł nam "0.8903030981660703".

print('punkt przecięcia z osią Y:', model.intercept_)

# Wyszedł nam -240.39174630009032 (to jest nasze b)

print('nachylenie:', model.coef_)

# Nasze nachylenie wynosi 0.13768894 (to jest nasze a)

# No i fajnie, teraz mamy prostą o równaniu y = 0.13768894 * x - 240.39174630009032.
z = 0.13768894 * 2000 - 240.39174630009032
print("Nasz wynik to wydajność {}% w roku 2000".format(z))
# No to teraz mamy równanie na naszą współrzędną y dla 0.13768894 * 2000 - 240.39174630009032. Wynik dodam do danych.




# Robię wykres:
plt.plot(x, y, 'o')
plt.title('Wykresik')
plt.xlabel("rok")
plt.ylabel("wydajnosc silnika (%)")
# Wypierdalam górną i lewą granicę wykresu zeby czysciej wyglądało:
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Zmieniam kolory prawej i dolnej bo czemu by nie
plt.gca().spines['left'].set_color('red')
plt.gca().spines['bottom'].set_color('green')

# Fajnie, działa. Dodaję prostą:
plt.plot(x, -240.39174630009032 + 0.13768894 * x, c='r', linewidth=1.5, alpha=0.2, solid_capstyle='round')

# I teraz dodam strzałkę pokazującą, gdzie jest nasz wynik
plt.annotate('a tutaj nasz aproksymalny wynik :)', xy=(2000, 34.98),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.1'), xytext=(1900, 36))

# A teraz dodam co jest co (jaki model silnika parowego) tak dla hecy
print("A teraz wymyśl jakąś ciekawą nazwę dla naszego hipotetycznego silnika parowego o wydajnosci którą zaraz wyliczy ci twoj mzodyfikowany zaliczeniowy program 3000 i tu se kurwa wpisz.")
hipotetyczna_nazwa = str(input("nazwy 'chuj', 'gej' i 'pedal' i ich wariacje odpadają. Wymysl cos lepszego blagam cie i nie sprawdzaj co sie stanie jak wpiszesz slowo 'gej' lub jego wariacje. Serio. Zabraniam. - "))
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
a = 0
podpisy_silnikow = ["Newcomen", "Smeaton", "Smeaton", "Watt", "Watt", "Woolf compound", "Improved cornish", "Improved Cornish", "Corliss compound", "Triple expansion", hipotetyczna_nazwa]

if "peda" not in hipotetyczna_nazwa:
    a = a + 1
if "homo" not in hipotetyczna_nazwa:
    a = a + 1
if "chuj" not in hipotetyczna_nazwa:
    a = a + 1
if "gej" not in hipotetyczna_nazwa:
    a = a + 1
if a == 4:
    print("Umiesz czytac i uzywac innych slow niz wszelakie okreslenia na homoseksualistów.")
    for i, label in enumerate(podpisy_silnikow):
        plt.annotate(label, (x[i] - 4, y[i] - 1))
    plt.show()
else:
    print("No i sie program wyjebal, debilu jebany. Nie umiesz podążać za instrukcjami?")
    print("naucz sie w koncu przyjmowac konsekwencje na klate jak prawdziwy mężczyzna a nie")


# No i elegancko. Se pobierz numpy i matplotliba bo inaczej moze byc ciezko.
# Czekam na frajernie.
