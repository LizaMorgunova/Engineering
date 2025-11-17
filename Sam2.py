def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as f:
        for _ in range(n):
            f.write(f"{a}\n")
            yield a
            a, b = b, a + b
fibonacci_numbers = list(fib(200))
print(fibonacci_numbers[199])
