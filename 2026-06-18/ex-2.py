# 2 - Função de Fibonacci com memorização.
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print("\n2. Fibonacci com memorização:")
print(" Fib(10):", fib(10))
print(" Fib(20):", fib(20))