a, b = map(int, input().split())
r = int(input())
n = int(input())
c = 0
for i in range(n):
    x, y = map(int, input().split())
    if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
        c += 1
print(int(c / n * 100))
