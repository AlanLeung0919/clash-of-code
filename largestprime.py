n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
x.sort(reverse=True)


def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


for i in x:
    if isPrime(i):
        print(i)
        break
