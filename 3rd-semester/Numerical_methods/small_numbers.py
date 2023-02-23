import numpy as np

x = 1/5
a = np.float32(x)

print(np.finfo(x))
print(np.finfo(a))
sum_1 = 0
sum_2 = 0
sum_3 = np.float32(0)
sum_4 = np.float32(0)
for i in range(1, 10_000):
    sum_1 += 1/(i**3)

for i in range(10_000, 0, -1):
    sum_2 += 1/(i**3)

for i in range(1, 10_000):
    sum_3 += np.float32(1/(i**3))

for i in range(10_000, 0, -1):
    sum_4 += np.float32(1/(i**3))

print(f'sum 1: {sum_1}, sum 2: {sum_2}')
print(f'sum 3: {sum_3}, sum 4: {sum_4}')


