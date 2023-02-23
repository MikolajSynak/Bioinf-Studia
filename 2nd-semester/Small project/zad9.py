import matplotlib.pyplot as plt
import numpy as np

# wpisuję dane i oznaczam je jako "x" i "y"
x = np.array([1.0, 2.5, 3.5, 4.0, 1.1, 1.8, 2.2, 3.7])
y = np.array([6.008, 15.772, 27.130, 33.772, 5.257, 9.549, 11.098, 28.828])

wsp = np.polyfit(x, y, 1, rcond=None, full=False, w=None, cov=False)
print(wsp)
# nasze "a" wynosi "9.43867546" a nasze "b" wynosi "-6.18397177". Wstawiam to zatem do równania y=ax+b i mam linię na moim wykresie:
plt.plot(x, y, 'o')
plt.plot(x, -6.18397177 + 9.43867546 * x, c='r', linewidth=1.5, alpha=0.2, solid_capstyle='round')
plt.show()
plt.plot(x, y, 'o')

#I teraz o co chodzi, "fit a straight line AND a quadratic and compere them"? Metodą "quadratic" wyliczyłem prostą linię idącą przez wykres. Czym się różnią te dwie metody?