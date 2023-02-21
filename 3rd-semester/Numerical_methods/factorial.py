def factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    return n * factorial(n-1)


n = input("Factorial for: ")
print(factorial(n))

# print(factorial(0))
# print(factorial(-1))
# print(factorial(2))
# print(factorial(5))
# print(factorial(12))