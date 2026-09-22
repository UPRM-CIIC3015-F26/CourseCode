import math

def calculate_lateral_area(radius, height):
    """
    Calculates the lateral (curved side) surface area of the barrel in square feet.

    Args:
        radius (float): The radius of the barrel's base in feet.
        height (float): The total height of the barrel in feet.

    Returns:
        float: The lateral surface area in square feet.
    """
    return height * (2 * math.pi * radius)

def calculate_lids_area(radius):
    """
    Calculates the combined surface area of the top and bottom lids in square feet.

    Args:
        radius (float): The radius of the barrel's lids in feet.

    Returns:
        float: The total area of both circular lids in square feet.
    """
    return 2 * (math.pi * radius **2)

def calculate_total_surface_area(radius, height):
    """
    Calculates the complete exterior surface area of the barrel in square feet.

    Args:
        radius (float): The radius of the barrel's base in feet.
        height (float): The total height of the barrel in feet.

    Returns:
        float: The sum of the lateral area and both lids in square feet.
    """
    return calculate_lateral_area(radius, height) + calculate_lids_area(radius)

def calculate_total_cost(radius, height, sq_ft_per_gallon, price_per_gallon):
    """
    Calculates the final cost to paint the entire exterior of the barrel.

    Args:
        radius (float): The radius of the barrel's base in feet.
        height (float): The total height of the barrel in feet.
        sq_ft_per_gallon (float): The area in square feet that one gallon of paint covers.
        price_per_gallon (float): The cost for one gallon of paint.

    Returns:
        float: The total calculated cost in dollars.
    """
    total_area = calculate_total_surface_area(radius, height)
    total_cost = total_area / sq_ft_per_gallon * price_per_gallon
    return total_cost

# --- Example Usage  ---
barrel_radius = 1.5
barrel_height = 5.0
sq_ft_per_gallon = 350
cost_per_gallon = 45.00

final_price = calculate_total_cost(barrel_radius, barrel_height, sq_ft_per_gallon, cost_per_gallon)
print(f"Total cost to paint the barrel: ${final_price:.2f}")