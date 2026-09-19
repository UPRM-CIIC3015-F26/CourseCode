"""
Logical simplification

Having many nested if statements can make a program harder to follow.
To make code easier to understand, when possible, we can reduce certain 
statements into a single condition using logical operators (AND, OR, and NOT)
"""
x = 10

# If x is divisible by 2
if x % 2 == 0:
    # If x also divisible by 3
    if x % 3 == 0:
        print("x is divisible by both 2 and 3")
    # Not divisible by 3
    else:
        print("x is divisible by 2")
else:
    # If x divisible by 3
    if x % 3 == 0:
        print("x is divisible by 3")
    # Not divisible by 2 or 3
    else:
        print("x isn't divisible by 2 or 3")