import scipy
import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import interp1d

x = np.linspace(0, 10, 11)
y = (np.cos(-x**2/9)+1)*50

f_linear = scipy.interpolate.interp1d(x, y)

x_new = np.linspace(0, 10, 100)

plt.scatter(x, y)
plt.plot(x_new, f_linear(x_new))
plt.title('Wykresik')
plt.ylabel("nie mam pojecia co oznaczają te dane")
plt.xlabel("naprawdę... ale gdybym wiedział to bym tu napisał;)")



plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_color('red')
plt.gca().spines['bottom'].set_color('green')

plt.show()
