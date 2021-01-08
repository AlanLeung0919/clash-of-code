n = int(input())
m = int(input())


def s(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return s(n - m, m) + s(n, m - 1)


print(s(n, m))
