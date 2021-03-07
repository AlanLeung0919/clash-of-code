def a(n):
    if n < 0.0001:
        return (n ** 2 - (n / 2) ** 2) ** (1 / 2) * n / 2
    return a(n / 2) * 4


n = int(input())
print(a(n))
