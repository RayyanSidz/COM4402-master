# 1. Repeat a Word
# word = input("Enter the word you want to repeat: ")
# n = int(input("Enter the number of times you want the word to repeat: "))
# for i in range(n):
#     print(f"{i+1}: {word}")

# 2. Sum of First N Numbers
# number = int(input("Enter the number to sum till: "))
# sum = 0
# for i in range(1, number + 1):
#     sum += i
# print(f"The sum from 1 to {number} is {sum}")

# 3.Multiplication Table
# x = int(input("Enter the number to get its multiplication table: "))
# for i in range(1, 11):
#     print(f"{i} x {x} = {i*x}")

# 4. Count Characters (Non-space)
# sentence = input("Enter a sentence to get a count of its characters: ")
# count = 0
# for i in sentence:
#     if i != ' ':
#         count+= 1
# print(f"The character count in the word is {count}")

# 5. Find Maximum Mark
# marksCount = int(input("Enter the number of marks: "))
#
# largestMark = float(input("Enter the first mark: "))
# for i in range(marksCount - 1):
#     newMark = float(input("Enter the next mark: "))
#     if newMark > largestMark:
#         largestMark = newMark
# print(f"The largest mark is {largestMark}")

# 6. Filter Passing Marks
# marksCount = int(input("Enter the number of marks: "))
#
# for i in range(marksCount):
#     marks = float(input("Enter marks: "))
#     if marks >= 40:
#         print(marks)
# print(f"The number of marks entered are: {marksCount}")

# Reverse a String (Manual)
# word = input("Enter the word to reverse: ")
# new_word = ""
# for i in range(len(word)):
#     new_word = new_word + word[len(word) - i - 1]
# print(new_word)

# Count Specific Letter in a List of Names
# nameCount = int(input("Enter the number of names to enter: "))
# nameList = []
# letter = input("Enter a letter to search: ")
# count = 0
#
# for i in range(nameCount):
#     nameList.append(input("Enter a name to add to the list: "))
#     if letter.lower() in nameList[i].lower():
#         count += 1
# print(f"The number of names containing the letter '{letter}' is {count}")

# Grade Statistics
# studentsCount = int(input("Enter the number of students: "))
# totalMarks = 0
# distinctionCount = 0
#
# for i in range(studentsCount):
#     marks = float(input("Enter marks between 0 and 100: "))
#     totalMarks += marks
#     if marks >= 70:
#         distinctionCount += 1
# print(f"Total marks are {totalMarks}\n"
#       f"average mark is {totalMarks / studentsCount}\n"
#       f"number of distinctions is {distinctionCount}")

# Simple Text-Based Bar Chart
# numberCount = int(input("Enter the count of numbers in a list: "))
#
# numberList = []
# for i in range(numberCount):
#     numberList.append(int(input("Enter the number to add to the list: ")))
#
# for j in numberList:
#     print('*' * j)

























