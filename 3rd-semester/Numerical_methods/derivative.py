import matplotlib.pyplot as plt
import numpy as np
import sympy as s


def derivative(f, start, end, step):
    h = 10**-5
    i = start
    ys = []
    while i <= end:
        y_prime = 1/(2*h) * (f(i+2*h) - f(i))
        ys.append(y_prime)
        i += step

    return ys


xs = np.linspace(-1.5, 1.5, num=30)
y_primes = derivative(lambda x: (x**3) + (4 * s.sin(x)) - (8 * x), -5, 5, 0.1)
plt.plot(xs, y_primes)
plt.show()