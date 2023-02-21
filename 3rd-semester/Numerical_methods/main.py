import numpy as np
from matplotlib import pyplot as plt

bacteries = np.loadtxt('bakterie.txt')
x = bacteries[:,0]
y = bacteries[:,1]
plt.plot(x,y)
plt.show()