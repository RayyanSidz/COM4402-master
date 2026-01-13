import math
for i in range(4):
    for j in range(4 - 1 - i):
        print(" ", end="")
    for n in range(4- 3 + i):
        print("*" , end="")
    for x in range(i):
        print("*", end= "")
    print()