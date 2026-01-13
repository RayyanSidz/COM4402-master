# Grade by score
# score = int(input("Enter your score: "))
# if score >= 70:
#     print("Distinction")
# elif score >= 40:
#     print("Pass")
# else:
#     print("Fail")

# Nested score
score = int(input("Enter your score: "))
if score >= 40:
    if score >= 70:
        print("Pass with merit")
    else:
        print("Pass")
else:
    print("Fail")