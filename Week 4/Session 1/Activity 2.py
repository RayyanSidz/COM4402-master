# Local vs Global Guess
# count = 0
# def add_one():
#  count = count + 1
#  print("Inside:", count)
# add_one()
# print("Outside:", count)

# Prediction: This would show an error because count isn't defined inside of the function
# Rewritten:
count = 0
def add_one(count):
    return count + 1
count = add_one(count)
print("Outside:", count)
