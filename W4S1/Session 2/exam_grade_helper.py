
def classify_mark(mark):
    if not isinstance(mark, int):
        raise TypeError("Invalid Type")
    if mark < 0 or mark > 100:
        raise ValueError("Mark outside range")
    if mark < 40:
        return "Fail"
    elif mark >= 40 and mark < 70:
        return "Pass"
    else:
        return "Distinction"

def calculate_summary(marks: list[int]):
    total = 0
    fail_count = 0
    average = 0.0
    distinction_count = 0
    for mark in marks:
        total += mark
        result = classify_mark(mark)
        if result == "Fail":
            fail_count += 1
        elif result == "Distinction":
            distinction_count += 1
    try:
        average = total / len(marks)
    except ZeroDivisionError:
        print("Can't divide by zero")

    return int(total), float(average), int(fail_count),int(distinction_count)




