from math import e, isclose


def bisection(f, a, b):
    epsilon = 10 ** -6
    i = 0
    while abs(a - b) > epsilon and i < 10 ** 6:
        if f(a) * f(b) < 0:
            mid = (a + b) / 2
            x = f(mid)
            if isclose(x, 0.0, abs_tol=epsilon):
                return mid
            if f(a) * f(mid) < 0:
                b = mid
            elif f(b) * f(mid) < 0:
                a = mid
        else:
            return None
        i += 1


print(f'(bisection) root {bisection(lambda x: e ** x - x ** 2 + 1, -3, 3)}')
print(f'(bisection) root {bisection(lambda x: e ** (x*10) - x ** 2 + 1, -3, 3)}')
print(f'(bisection) root {bisection(lambda x:  x ** 2 + 1, -10, 10)}')


def newtons(f, f_prime, x0):
    epsilon = 10 ** -8
    max_iterations = 10**6
    for i in range(max_iterations):
        y = f(x0)
        y_prime = f_prime(x0)

        if abs(y_prime) < epsilon:
            break
        x1 = x0 - (y / y_prime)
        if abs(x1 - x0) <= epsilon:
            return x1

        x0 = x1

    return None


print(f'(Newtons) root (guess: 0) {newtons(lambda x: (x-3)*(x+2), lambda x: 2*x-1, 0)}')
print(f'(Newtons) root (guess: -1) {newtons(lambda x: (x-3)*(x+2), lambda x: 2*x-1, -1)}')
print(f'(Newtons) root (guess: 2) {newtons(lambda x: (x-3)*(x+2), lambda x: 2*x-1, 2)}')

