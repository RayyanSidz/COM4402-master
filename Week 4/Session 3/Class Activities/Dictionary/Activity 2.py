
courses = {
    "python": {
        "students": ["Ali", "Sara", "Tom", "Ali"],
        "max_size": 3
    },
    "datasci": {
        "students": ["Sara", "Imran"],
        "max_size": 2
    }
}

# 1. For each course, print the set of unique student names (so each name appears once).
# 2. For each course, check if the number of unique students is greater than `max_size`
# and print `"FULL"` or `"OK"`.
# 3. Build a dictionary `student_counts` mapping each student name to
# how many different courses they are enrolled in (use a dict plus sets or lists).

# 1)
print(courses)
print(courses["python"])
print(courses["python"]["students"])
print(courses["python"]["students"][0])

