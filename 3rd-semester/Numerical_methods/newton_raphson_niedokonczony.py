import sympy as s

def f(x):
    return s.tan(x) + (x + 1) * (x + 1)

# Pochodna:
def g(x):
    return s.sec(x) * s.sec(x) + 2 * (x + 1)

epsilon = 0.0000001

def newtons(f, g, x0):
    epsilon = 10 ** -8
    imax = 10**6
    for i in range(imax):
        y = f(x0)
        y_prime = g(x0)

        if abs(y_prime) < epsilon:
            break
        x1 = x0 - (y / y_prime)
        if abs(x1 - x0) <= epsilon:
            return x1

        x0 = x1

    return None

newtons( f, g, -1)


