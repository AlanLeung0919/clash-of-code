b = int(input())
n = int(input())
e = b
for i in range(n - 1):
    e = b ** e
print(e)
