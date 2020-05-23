def f(x, y, n):
    if n <= 1:
        return x + x * y
    else:
        return f(x, y, n - 1) + f(x, y, n - 1) * y


print(f(1000, 0.01, 365))
