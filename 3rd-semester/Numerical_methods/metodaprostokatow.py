import sympy as s
import scipy

# Input użytkownika
a = float(input("Podaj dolny limit całkowania: "))
b = float(input("Podaj górny limit całkowania: "))
c = int(input("Podaj liczbę podprzedziałów: "))


# Nasza funkcja
def f(x):
    return (x * x * x) + (4 * s.sin(x)) - (8 * x)


# Metoda trapezów
def trapezownia(x0, xn, n):
    # liczenie zmiennej h (odległość między trapezami)
    h = (xn - x0) / n

    # Suma dolnej i górnej granicy
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h
        integration = integration + 2 * f(k)

    # Ostateczna wartość całki:
    integration = integration * h / 2

    return integration


# Wywołuję funkcję trapezownia() i dostaję wynik:

result = trapezownia(a, b, c)

print("Twój wynik to: {}".format(result))
