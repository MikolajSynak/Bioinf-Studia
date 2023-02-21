#Policz całki metoda trapezów i prostokątów:

import scipy as scp
import scipy.integrate as integrate
import scipy.special as special
import numpy as np
from math import sin, exp, pi
import math


# metodą prostokątów:

def integrate(function, a, b, i):
    dx = (b - a) / i
    integr = 0
    for x in range(i):
        x = x * dx + a
        integr += dx * eval(function)
    return integr

def main(args):
    function = input("Funkcja: ")
    a = float(input("Początek przedziału: "))
    b = float(input("Koniec przedziału: "))
    i = int(input("Liczba podprzedziałów: "))
    print("Całka z funkcji {funkcjon} po przedziale od {a} do {b} = {integrate}".format(funkcjon = function, a = a, b = b, integrate = integrate(function, a, b, i)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
#a teraz metoda trapezów:
    
