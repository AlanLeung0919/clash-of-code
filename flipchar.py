a = input()
b = input()
x = input()
y = x.replace(b, a)
z = x.replace(a, b)
for i in range(len(x)):
    if y[i] != x[i]:
        print(y[i], end="")
    else:
        print(z[i], end="")
