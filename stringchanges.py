n = input()
print(len([i for i in range(len(n) - 1) if n[i] != n[i + 1]]))
