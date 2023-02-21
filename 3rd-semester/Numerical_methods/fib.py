def fibb(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    return fibb(n-1) + fibb(n-2)


n = 0
while True:
    current_fibb = fibb(n)
    if current_fibb >= 1000:
        break
    print(current_fibb)
    n += 1
