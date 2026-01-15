students = {
     "Aisha": 85,
     "Bilal": 72,
     "Chen": 90
}

def find_mark(students, name):
    if not type(students) == dict:
        raise TypeError("Invalid datatype")
    if not type(name) == str:
        raise TypeError("Invalid datatype")
    if name in students:
        return students[name]
    return None

