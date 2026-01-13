Triangle = [[1],
            [1,1]]
for i in range(2, 5):
    Triangle.append([])
    for j in range(i+1):
        if j > 0 and j != (len(Triangle[i-1])):
            Triangle[i].append(Triangle[i - 1][j] + Triangle[i - 1][j - 1])
        else:
            Triangle[i].append(1)


for i in Triangle:
    print(i)

