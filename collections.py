# Collections

# Lists

# First List = shopping list
# [] = list
# shopping_list = ["milk", "bread", "eggs", "chocolate", "jam"]
#
# print(shopping_list)
#
# # Accessing a particular part of the list
# print(shopping_list[-1])
#
# # change an element in a list
# shopping_list[2] = "butter"
# print(shopping_list)
#
# # Using List Methods
#
# # adding to a list with append()
# shopping_list.append("Fish")
# print(shopping_list)
#
# # removing items with remove()
# shopping_list.remove("bread")
# print(shopping_list)
#
# # removing the last item from a list, without specifying what it is
# shopping_list.pop()
# print(shopping_list)

# Can I have a list with mixed data types
mixture = [1, 2, 3, 4.5, "five", "six"]
print(mixture)

# Slicing
print(mixture[1:3])

# Reverse order of slice
print(mixture[-3::2])

# step over
print(mixture[3::])

# Tuples
# Tuples are immutable - cannot be changed

# tuple_example = ("bread", "eggs", "milk")
# print(tuple_example)
# tuple_example(0) = "cheese"

## Dictionaries

# Another way to manage data, but they are a little bit more dynamic and complex

# Key - Value pairs

# Key = reference to object
# Value = data mechanism you wish to store data in (eg. string, int, list, anotehr dictionary)

student_1 = {
    "name": "Luke",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data types", "setup"]
}

# Access the dictionary

print(student_1["stream"])

# Access a part of the list in the dictionary
print(student_1["completed_lesson_names"][0])

# Changing a value

student_1["completed_lessons"] = 4
print(student_1["completed_lessons"])

# Changing an element of a list within a dictionary

student_1["completed_lesson_names"].remove("data types")
print(student_1["completed_lesson_names"])

# Dictionary Methods

print(student_1.keys())
print(student_1.values())

# Sets and Frozen sets

# set in python is a list that has no order/indexing

car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)

car_parts.add("windows")
print(car_parts)

car_parts.discard("doors")
print(car_parts)

# Frozen sets
# Immutable set, cant change anything about it

x = frozenset([1, 2, 3, 4])

print(x)



















