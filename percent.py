n = int(input())
c = 0
for i in range(n):
    c += input().count("*")
print(c * 100 // (n * n) if n > 0 else 0, sep="")
