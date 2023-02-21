import time
start = time.time()

import numpy as np

lista1 = range(1, 10000)
suma1 = sum(lista1)
print(suma1)
x = 0
for i in lista1:
    x += 1/(i**3)
x = np.float32(x)
print(x)
end = time.time()
print("czas liczenia: ",
      (end-start) * 10**3, "ms")

# float64: 1.202056898159098
# float32: 1.2020569
