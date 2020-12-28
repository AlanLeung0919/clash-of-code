s = input()
r = s[::-1]
for i in range(len(s)):
    print(s[i] + r[i], end="")
