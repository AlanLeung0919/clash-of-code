n = int(input())
s = int(input())
for i in range(n):
    c = s
    for j in range(i):
        print(str(c), end=" ")
        c = int(c * (i - j - 1) / (j + 1))
    print()
