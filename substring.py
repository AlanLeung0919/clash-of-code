n = int(input())
s = input()
for i in range(len(s) - n + 1):
    print(s[i : i + n])
