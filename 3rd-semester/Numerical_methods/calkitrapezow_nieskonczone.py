import matplotlib.pyplot as plt
import numpy as np
import scipy

def integral_rect(f, start, stop, step=0.1):


def trapezoidal_rule(fun, a, b, n):
    y = []
    i = start
    while i <= step:
        val = (f(i) + f(i + step) *  step)/2
        y.append(val)
        i += step


x = trapezoidal_rule(y, 0.0, 1.0, 100)

print(sum(x))
