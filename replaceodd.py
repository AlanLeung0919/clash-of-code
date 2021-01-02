s = str(sum(map(int, input())) * 2)
print(*(i if int(i) % 2 == 0 else "@" for i in s), sep="")
