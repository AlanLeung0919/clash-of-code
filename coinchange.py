n = int(input())
s = int(input())
c = []
r = [0] * (n + 1)
r[0] = 1
for i in input().split():
    c += [int(i)]
for i in c:
    for j in range(1, n + 1):
        if j >= i:
            r[j] += r[j - i]
print(r[-1])
