x = []
n = int(input())
for i in range(n):
    x.append(input())
x.sort(key=len)
for i in x:
    print(i)
