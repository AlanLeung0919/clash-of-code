n = int(input())
s = int(input())
c = 0
for i in range(n):
    c += input().count("o")
print(c * s)
