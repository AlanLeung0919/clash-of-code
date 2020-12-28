x, y = input().split()
for i in range(len(x)):
    if x[i] == "1" or y[i] == "1":
        print(1, end="")
    else:
        print(0, end="")
