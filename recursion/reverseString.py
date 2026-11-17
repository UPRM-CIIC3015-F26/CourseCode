def reverse_str(s):
    """
    Recursively reverses a string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    if len(s) <= 1:
        return s
    else:
        return reverse_str(s[1:]) + s[0]
    

name = "cat"
print(f"The word {name} when reversed is {reverse_str(name)}")
