def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fibonacci_numbers = list(fib(200))
print(fibonacci_numbers[199]) 
