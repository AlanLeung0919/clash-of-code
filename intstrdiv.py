s = input()
x = 0
y = 0
for i in s:
    if i.isalpha():
        x += 1
    elif i.isdigit():
        y += 1
print(round(x / y))
