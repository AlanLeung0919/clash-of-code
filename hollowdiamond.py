h = (int(input()) - 1) // 2
w = 1 + h * 2
for i in range(h + 1):
    if i == 0:
        print("*".center(w))
    else:
        n = 1 + (i - 1) * 2
        print(f"*{' ' * n}*".center(w))
for i in range(h):
    if i == h - 1:
        print("*".center(w))
    else:
        n = 1 + (h - 1 - i - 1) * 2
        print(f"*{' ' * n}*".center(w))
