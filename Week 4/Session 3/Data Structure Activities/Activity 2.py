seats = []
def create_row(names):
    """Create a seating row from a list of names."""
    global seats
    seats = names.copy()


def get_student_at(index):
    """Return the student at a given seat index, or None if invalid."""
    global seats
    return seats[index]

def swap_seats(index1, index2):
    """Swap the students at two positions."""
    global seats
    seats[index1], seats[index2] = seats[index2], seats[index1]

def remove_student(name):
    """Remove the first occurrence of a student by name."""
    global seats
    seats.remove(name)

names = ["Rayyan", "Dante", "Kratos"]
create_row(names)
student = get_student_at(1)
print(student)
print(seats)
swap_seats(0, 1)
print(seats)
remove_student("Kratos")
print(seats)



