import matplotlib.pyplot as plt
import numpy as np

x = np.array([1718, 1767, 1774, 1775, 1792, 1816, 1828, 1834, 1878, 1906]).reshape((-1, 1))
y = np.array([0.5, 0.8, 1.4, 2.7, 4.5, 7.5, 12.0, 17.0, 17.2, 23.0])


def linear_regression(a, b):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean) ** 2).sum()
    B1 = B1_num / B1_den

    B0 = y_mean - (B1 * x_mean)

    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))

    return B0, B1, reg_line


linear_regression(x, y)


def corr_coef(x, y):
    N = len(x)

    num = (N * (x * y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x ** 2).sum() - x.sum() ** 2) * (N * (y ** 2).sum() - y.sum() ** 2))
    R = num / den
    return R


corr_coef(x, y)


def predict(B0, B1, new_x):
    y = B0 + B1 * new_x
    return y


predict(8.660000000000045, 346.02833200672546, 2010)

B0, B1, reg_line = linear_regression(x, y)
print('Regression Line: ', reg_line)
R = corr_coef(x, y)
print('Correlation Coef.: ', R)
print('"Goodness of Fit": ', R ** 2)

plt.plot(x, y, 'o')
plt.title('Wykresik')
plt.xlabel("rok")
plt.ylabel("wydajnosc silnika (%)")
plt.plot(x, -240.39174630009032 + 0.13768894 * x, c='r', linewidth=5, alpha=0.5, solid_capstyle='round')

plt.show()
