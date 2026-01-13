# 1. Cinema Ticket Category
# age = int(input("Enter your age: "))
# if age >= 65:
#     print("Senior Ticket")
# elif age >= 18:
#     print("Adult ticket")
# elif age >= 5:
#     print("Child ticket")
# else:
#     print("Free entry")


# 2. Library Fine Calculator
# days_late = int(input("Enter number of days late: "))
# if days_late ==  0:
#     print("No fine")
# elif days_late <= 5:
#     print("Fine = £1")
# elif days_late <=10:
#     print("Fine = £5")
# else:
#     print("Fine = £10 and membership review")


# 3. Exam Borderline Check (Nested)
# score = int(input("Enter a score between 0 and 100: "))
# if score >= 40:
#     if score <= 42:
#         print("Borderline Pass")
#     else:
#         print("Clear pass")
# else:
#     print("Fail")


# 4. Discount Eligibility
# is_student = input("Are you a student, Yes or No: ")
# age = int(input("Enter age: "))
# if is_student.lower() == "yes" or age < 18:
#     print("Discount applied")
# else:
#     print("No discount")

# 5. Traffic Light Action
# color = input("Enter color: ").lower()
# if color == "red":
#     print("Stop")
# elif color == "amber":
#     print("Get ready")
# elif color == "green":
#     print("Go")
# else:
#     print("Invalid color")

# 6. Multiple of 3, 5 or Both
# number = int(input("enter a number: "))
# if number % 3 == 0 and number % 5 == 0 and number != 0:
#     print("fizzbuzz")
# elif number % 3 == 0 and number != 0:
#     print("fizz")
# elif number % 5 == 0 and number != 0:
#     print("buzz")
# else:
#     print("no match")


# 7. Meal Recommedation (Nested)
# is_hungry = input("is it hungry, yes or no: ").lower()
# if is_hungry == "no":
#     print("Have some water and rest")
# elif is_hungry == "yes":
#     time_of_day = input("Enter a time of day, morning, afternoon or evening: ").lower()
#     if time_of_day == "morning":
#         print("Have Breakfast")
#     elif time_of_day == "afternoon":
#         print("Have Lunch")
#     elif time_of_day == "evening":
#         print("Have dinner")
#     else:
#         print("Snack time")
# else:
#     print("Invalid")


# 8. Module Mark Status
# courseMark = int(input("Enter course marks: "))
# examMark = int(input("Enter exam mark: "))
# if courseMark < 35 or examMark < 35:
#     print("Automatic fail (component beblow 35)")
# elif ((courseMark + examMark) / 2) >= 40:
#     print("Module passed")
# else:
#     print("Module failed (average below 40)")

# 9. Simple Two-Stage Verification




choice = int(input("What's 8 * 9? 1. 89, 2. 24, 3. 27, 4. 72? \n"))

match choice:
    case 1:
        print("Incorrect")
    case 2:
        print("Incorrect")
    case 3:
        print("Incorrect")
    case 4:
        print("Correct")
    case _:
        print("Cosmin sucks at aba")






