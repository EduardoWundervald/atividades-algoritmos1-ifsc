# 13 - Função que calcula o n-ésimo termo de Fibonacci.
def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

print("\n13. Fibonacci(7):", fibonacci(7))
print(" Fibonacci(10):", fibonacci(10))