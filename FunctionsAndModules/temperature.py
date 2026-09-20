def celsius_to_farenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def farenheit_to_celsius(farenheit):
    """Convert temperature from Fahrenheit to Celsius.

    Args:
        farenheit (float): Temperature in Fahrenheit

    Returns:
        float: Temperature in Celsius
    """
    return (farenheit - 32) * 5 / 9
