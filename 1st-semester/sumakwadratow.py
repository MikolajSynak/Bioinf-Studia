from math import ceil, sqrt
def sumakwadratow(n):
 for x in range(0,ceil(sqrt(n)+1)):
    for y in range(x,ceil(sqrt(n)+1)):
        for z in range(y,ceil(sqrt(n)+1)):
            if n == x * x + y * y + z * z :
                print(x, y, z)
print(sumakwadratow(128))