sign = "00000000000"

counter = len(sign)
for x in range(len(sign)):
    print(sign[0:x])

for x in range(len(sign)):
    print(sign[0:(counter-x)])


print("\nOR\n")

for x in range(1,12):
    print("0"*x)

for x in range(12,0,-1):
    print("0" * x)