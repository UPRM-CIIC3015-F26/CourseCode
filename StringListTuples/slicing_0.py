example = "Python"

# First Letter
print(example[0])
# Last Letter
print(example[-1])
# Reverse
print(example[::-1])
# First Three
print(example[0:2])
# 3 to the end
print(example[3:])
# Letters on Even Position
# (indices 0, 2, 4 -> 'P', 't', 'o')
print(example[::2])

#  Letters on Odd Position
# (indices 1, 3, 5 -> 'y', 'h', 'n')
print(example[1::2])