def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = 5

print("Generator Output:")
for num in fibonacci_generator(n):
    print(num)
