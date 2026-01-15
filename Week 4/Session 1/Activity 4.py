# Parameter vs Global

# Version 1
rate = 0.2
def calculate_tax(amount):
    return amount * rate
print(calculate_tax(10.0))

# Version 2
def calculate_tax(amount, rate):
    return amount * rate
print(calculate_tax(10.0, 0.2))

# rate can be set to what you want in the function call itself, rather then updated the global variable each time
