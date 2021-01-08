n = list(map(int, input().split()))
x = {}
for i in n:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1
print(max(x, key=x.get))
