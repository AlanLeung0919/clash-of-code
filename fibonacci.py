n = int(input())
x = int(input())
y = int(input())
print(x)
print(y)
for i in range(n):
    z = x + y
    x = y
    y = z
    print(z)
