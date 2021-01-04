n = list(map(int, input().split()))
print("true") if max(n) <= sum(n) - max(n) else print("false")
