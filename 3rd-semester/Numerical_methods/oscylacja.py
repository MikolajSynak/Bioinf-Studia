import matplotlib.pyplot as plt
from numpy import array, zeros, arange

k = 2
m = 1


def Oscillation(state):
    v0 = state[1]
    a = (-k/m) * state[0]
    return array([v0, a])


def Euler(y, derivative):
    y_next = y + derivative(y) * dt
    return y_next


x0 = 10 # initial conditions
v0 = 0
dt = 0.05

#masz na zdjęciach kod





