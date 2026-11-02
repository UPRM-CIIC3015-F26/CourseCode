def get_path(start: int) -> list:
    """
        Returns the path from the start value until reaching 1, following the rules of the Collatz conjecture.

        Rules:
        - If the current number is even, divide it by 2.
        - If the current number is odd, multiply it by 3 and add 1.

        Args:
            start (int): The starting value for the path.
        
        Returns:
            list: A list containing the path from the start value to 1.
    """
    

value = 10
print(f"The path from {value} to 1 is: {get_path(value)}")