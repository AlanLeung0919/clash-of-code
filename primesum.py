n = int(input())


def isPrime(number):
    if n < 2:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1


x = []
for i in range(n):
    a = int(input())
    if isPrime(a):
        x += [a]
print(sum(x))
