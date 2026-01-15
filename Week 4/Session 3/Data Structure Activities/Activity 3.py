course = {}
current_modules = {"CS", "MA", "SC", "AR"}

def enrol_module(modules, code):
    """Add a module code if not already present."""
    if code in modules:
        print("Already enrolled")
    else:
        modules.add(code)
    print(f"Enrolled: {modules}")
    return modules

# enrol_module(current_modules, "SC")


def is_enrolled(modules, code):
    """Return True if the student is enrolled on this module."""
    if code in modules:
        print("Already enrolled")
        return True
    else:
        print("NOT enrolled")
        return False

# is_enrolled_sc = is_enrolled(current_modules, "SC")
# print(is_enrolled_sc)


def drop_module(modules, code):
    """Remove a module if present."""


def count_modules(modules):
    """Return how many modules the student is taking."""

