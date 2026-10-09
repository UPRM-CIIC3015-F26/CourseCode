numbers = [10, -5, 20, -3, 15, 30]

# Print all list elements and their positions (while, range and enumerate)

def print_all_numbers_while(nums):
    index = 0
    while index < len(nums):
        print(nums[index])
        index +=1

def print_all_numbers_range(nums):
    for i in range(len(nums)):
        print(nums[i])


def print_all_numbers(nums):
    for x in nums:
        print(x)


print_all_numbers_while(numbers)

print_all_numbers_range(numbers)


print_all_numbers(numbers)

# Get total sum of numbers in a list

def sum_numbers(nums):
    return sum(nums)

print(f"Sum: {sum_numbers(numbers)}")


# Get total sum of numbers in a list at even positions

def sum_at_even(nums):
    pass

print(f"Sum at Even: {sum_at_even(numbers)}")

# Get average of numbers in a list

def average(nums):
    pass

print(f"Average: {average(numbers)}")

average(numbers)
# Find largest number within a list

def find_largest_number(nums):
    pass

print(f"Largest Number:{find_largest_number(numbers)}")

# Determine is a number exists in a list
def number_in_list(nums, item):
    pass

print(f"Number in list: {number_in_list(numbers, 20)}")

# Find the position of a number in a list

def index_in_list(nums, item):
    pass

print(f"Position in list: {number_in_list(numbers, 20)}")

# Filter even numbers from a list

def filter_even_numbers(numbers):
    pass
print(f"Filter even Numbers: {filter_even_numbers(numbers)}")


# Replace negative numbers with a replacement number

def replace_negative_numbers(nums, replacement):
    pass 

    print(f"Replace Negative Numbers: {replace_negative_numbers([1,-4, 10, -7, 15], 0)}")