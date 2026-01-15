list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = []

for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
print(list3)
print()
list3[1] = 99
list3[2] = 100
list3.remove(list3[3])
for i in range(2):
    list3.remove(list3[-1])
for i in range(len(list3)):
    list3[i] = list3[i] * 2

print(list3)