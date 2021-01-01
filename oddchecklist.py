x = [int(i) for i in input().split()]
for i in x:
    print(f"[x] {i}") if i % 2 != 0 else print(f"[ ] {i}")
