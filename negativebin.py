n = input()
c = 0
for i in range(len(n)):
    c += (-2) ** (len(n) - 1 - i) * int(n[i])
print(c)
