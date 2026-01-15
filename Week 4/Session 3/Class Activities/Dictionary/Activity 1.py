person = {
    "name" : "Sam",
    "city" : "London"
}

person["age"] = 21
person["city"] = "Bolton"
print(person)
person["age"] = int(input("Enter a new age: "))

for i in person:
    print(f"{i} : {person[i]}")

