# Complete the Function
def area_of_rectangle(width, height):
    # TODO: calculate the area
    return width * height

w = float(input("Enter width: "))
h = float(input("Enter height: "))

print(area_of_rectangle(w, h))

# w and h are Global variables, I didn't use any local variable but if I assigned area = width * height separately
# in the function, that would be the local variable
