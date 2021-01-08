n = int(input())
m = int(input())


def s(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return s(n - 1, m) + s(n, m - 1)


print(s(n, m))
