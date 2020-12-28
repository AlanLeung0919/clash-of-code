m = input()
y = "JFMAMJJASOND" * len(m)
print(y[y.find(m) + len(m)])
