n = int(input())
for i in range(n):
    x = input()
    for j in x:
        print("-", end="") if j != "1" else print(j, end="")
    print()
