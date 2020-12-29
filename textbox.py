x = input().split()
s = " " + x[0] + " "
c = x[1]
n = int(x[2])
x = n * 2 + len(s)
y = n * 2 + 1
for i in range(y):
    for j in range(x):
        if i == n:
            if j >= n and j < x - n:
                print(s[j - n], end="")
            else:
                print(c, end="")
        else:
            print(c, end="")
    print(end="\n")
