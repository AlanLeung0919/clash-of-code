x = [x for x in input()]
print(round(sum(ord(c) for c in x) / len(x), 1))
