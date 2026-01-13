#Activity 8
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
print("Hello ", name)
print("Next year you will be ", str(age + 1))
print("Your height is ", str(height), " metres")
print("age is of type ",type(age))
print("height is of type ", type(height))

#Activity 10
# Name = input("Enter your name: ")
# AGE = input("Enter your age: ")
# age_next_year = AGE +
# print("hello", Name, "next year you will be", age_next_year)

# Correct version
name = input("Enter your name: ")
age = int(input("Enter your age: "))
age_next_year = age + 1
print("hello ", name, " next year you will be ", str(age_next_year))
