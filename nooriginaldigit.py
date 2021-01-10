n = int(input())
m = str(n)
while sum(0 if i not in m else 1 for i in str(n)) != 0:
    n += 1
print(n)
