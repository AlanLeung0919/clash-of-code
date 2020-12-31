x = sorted(list(map(int, input().split())))
y = [[x[0]]]
z = []
for i in x[1:]:
    if i - y[-1][-1] > 1:
        y += [[i]]
    else:
        y[-1] += [i]
for i in y:
    z += [str(i[0]) if len(i) == 1 else str(i[0]) + "-" + str(i[-1])]
print(",".join(map(str, z)))
