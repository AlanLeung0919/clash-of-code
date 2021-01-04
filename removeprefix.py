p = [
    "Dr",
    "Mr",
    "Mrs",
    "Ms",
    "Lord",
    "Lady",
    "Sir",
    "BA",
    "LLB",
    "MD",
    "PhD",
    "Jr",
    "Snr",
]
n = int(input())
for i in range(n):
    x = input().split()
    for j in x:
        if not j in p:
            print(j[:1] + ".", end="")
    print()
