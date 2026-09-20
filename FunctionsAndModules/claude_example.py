def farenheit_to_celsius(farenheit):
    """Convert farenheit to celsius.
    
    Args:
        farenheit (float): The temperature in farenheit

    Returns:
        The temperature in celsius.
    """
    return (farenheit - 32) * 5 / 9


print(help(farenheit_to_celsius))