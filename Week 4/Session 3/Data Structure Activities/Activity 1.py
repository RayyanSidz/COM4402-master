def add_mark(marks, name, mark):
 """Add or update a student's mark."""
 marks[name] = mark
 return marks

def get_mark(marks, name):
 """Return a student's mark, or None if not found."""
 if name in marks:
     return marks[name]
 return None

def update_mark(marks, name, new_mark):
 """Update a student's mark if they exist."""
 if name in marks:
     marks[name] = new_mark
     return True
 return False
def delete_mark(marks, name):
 """Remove a student's mark if they exist."""
 if name in marks:
     del marks[name]
     return True
 return False



