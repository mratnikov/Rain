def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
n = int(input())
k = int(input())
print(factorial(n) // (factorial(k) * factorial(n - k)))
