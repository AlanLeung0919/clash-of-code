n, g = [int(i) for i in input().split()]
m = int(input())
x = [m]
for i in range(n):
    x.append(int(input()))
x.sort(reverse=True)
print(x.index(m) < g)
