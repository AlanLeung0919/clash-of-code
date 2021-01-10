n = float(input())
if n % 1 == 0:
    print(int(n))
else:
    for i in range(2, 1000000):
        if n * i % 1 == 0:
            print(f"{int(n * i)} / {i}")
            break
