x = list(map(int, input().split()))
y = list(set(x))
print(True) if len(x) == len(y) else print(False)
