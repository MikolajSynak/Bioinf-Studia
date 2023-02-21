import matplotlib.pyplot as plt
import numpy as np
import scipy

xnew = np.linspace(0, 10, 100)
y = (np.cos(-xnew**2/9)+1)*50
h = xnew[1] - xnew[0]

f_linear = scipy.interpolate.interp1d(xnew, y)

N = len(xnew)
speed = np.zeros(N)
zero = np.zeros(N)

bac_cubic = f_linear(xnew)

for i in range(1, N-1):
    speed[i] = 0.5*(bac_cubic[i+1] - bac_cubic[i-1])/h

plt.subplot(2,1,1)
plt.plot(xnew, y, 'x', xnew, f_linear(xnew), "--x")
plt.subplot(2,1,2)
plt.plot(xnew, zero, '--', xnew[1:N-1], speed[1:N-1], 'o-')
plt.show()