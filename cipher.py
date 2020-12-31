s = input()
k = int(input())
x = ""
for i in s:
    print((ord(i) - k - 65) % 65)
    if i != " ":
        x += chr((ord(i) - k - 65) % 26 + 65)
    else:
        x += " "
print(x)
