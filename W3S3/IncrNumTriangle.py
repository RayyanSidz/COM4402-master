currentNum = 1
for i in range(4):
    for j in range(i+1):
        print(f"{currentNum}", end = "")
        currentNum += 1
    print()