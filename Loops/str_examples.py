# Function receives a string and returns the last valid position in the string
def find_last_position(s):
    length_of_str = len(s)
    return length_of_str - 1


str = "This is awesome"
str2 = "cat"
str3 = "Hello!"

print(f"{str} : has {len(str)} characters")
pos = 11
print(f"At position {pos} we have the character {str[pos]}")

print(f"the last valid position for {str} is {find_last_position(str)}")
print(f"the last valid position for {str2} is {find_last_position(str2)}")
print(f"the last valid position for {str3} is {find_last_position(str3)}")