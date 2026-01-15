def group_marks(marks):
    """
    Group marks into 'Fail', 'Pass', and 'Distinction'.
    marks: list of integers (0..100)
    Returns a dict:
    {
    "Fail": [...],
    "Pass": [...],
    "Distinction": [...]
    }
    Raise TypeError if marks is not a list or if any element is not int.
    Raise ValueError if any mark is outside 0..100.
    """

    if type(marks) != list:
        raise TypeError("Invalid Datatype")
    failList = []
    passList = []
    distinctionList = []
    for mark in marks:
        if type(mark) != int:
            raise TypeError("Invalid Datatype")
        if mark < 0 or mark > 100:
            raise ValueError("Out of range")
        if mark < 40:
            failList.append(mark)
        elif 40 <= mark < 70:
            passList.append(mark)
        else:
            distinctionList.append(mark)

    return {
        "Fail" : failList,
        "Pass" : passList,
        "Distinction" : distinctionList
    }


