a, b = map(int, input().split())
x, y = map(int, input().split())
r = 0
while a > 0 and x > 0:
    a -= y
    x -= b
    r += 1
print(1 if a > x else 2, r)
