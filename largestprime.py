n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
x.sort(reverse=True)
for i in x:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
            break
    else:
        pass
