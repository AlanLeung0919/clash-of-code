x, y = input().split()
for i, v in enumerate(x):
    print(int(v) ^ int(y[i]), end="")
