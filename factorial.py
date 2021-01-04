n = int(input())
if n == 0:
    print(1)
else:
    f = n
    for i in range(n - 1):
        f = f * (i + 1)
    print(f)
