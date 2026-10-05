# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Single ITem Tuple
single_item = ("apple",)  # Note: trailing comma is required for single-item tuples
print("Single item tuple:", single_item)

# Multiple item tuple
fruits = ("apple", "banana", "cherry", "orange")
print("Multiple item tuple:", fruits)

# Access Elements in a Tuple
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

# Try to update a Tuple
try:
    fruits[0] = "mango"
except TypeError as error:
    print("Cannot update tuple (tuples are immutable!):", error)

# Swap Numbers
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap:  a = {a}, b = {b}")

# Return a Multiple Values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 2, 9, 1, 7])
print(f"Returned multiple values -> Min: {low}, Max: {high}")

# List to tuple
my_list = [1, 2, 3, 4]
converted_tuple = tuple(my_list)
print("List to tuple:", converted_tuple)

# Tuple to list
my_tuple = (5, 6, 7, 8)
converted_list = list(my_tuple)
print("Tuple to list:", converted_list)