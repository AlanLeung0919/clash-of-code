n = str(int(input()) + 1)
for i in range(len(n) - 1):
    if n[i] > n[i + 1]:
        break
print(n[:i] + n[i] * (len(n) - i))
