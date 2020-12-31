m = int(input())
h = int(input())
w = m + (h - 1) * 2
for i in range(h):
    n = m + i * 2
    s = (w - n) // 2
    print(f"{' ' * s}{'*' * n}{' ' * s}" * 2)
