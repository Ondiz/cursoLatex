def fibonacci(num):
    a = 0
    yield a
    b = 1
    yield b
    for i in range(num):
        (a,b) = (b, a + b)
        yield b

fibo = fibonacci(5)

for i in fibo:
    print(i)
