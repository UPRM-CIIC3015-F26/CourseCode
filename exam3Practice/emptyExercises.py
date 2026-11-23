"""
Statistics!
Receives a list of ages and calculates the max, min an average integers 
from the list. Return the max, min and average in a dictionary.

The keys in the returned dictionary should be: max, min, and average.
"""
def get_statistics(values: list) -> dict:
    pass


values1 = [10, 5, 34, 89, 23, 9, 2, 7]
print(f"For values: {values1}\nResults are: {get_statistics(values1)}\n")
values1 = [7, 7, 7, 7, 7, 7, 7]
print(f"For values: {values1}\nResults are: {get_statistics(values1)}")
print("="*80)

"""
Decipher message
Receives a dictionary that acts as a codex and a coded string.
Return the converted message using the codex to swap the original 
word with the new one.

Example:
codex= {
    "Bye": "Hello",
    "Friend": "World"
}
coded_message = "Bye Bye Friend"
decipher_message(codex, coded_message) should return "Hello Hello World"

Asume:
- All words in the message are in the codex
- All the words are separated by a whitespace

Convert the message in the order the words appear in the coded string.
"""
def decipher_message(codex: dict, coded_message:str) -> str:
    pass

codex= {
    "Bye": "Hello",
    "Friend": "Worlds"
}
coded_message = "Bye Bye Friend"
print(f"For the coded message \"{coded_message}\" the real message was: {decipher_message(codex, coded_message)}\n")

codex= {
    "^": "UP",
    "v": "DOWN",
    "<": "LEFT",
    ">": "RIGHT"
}
coded_message = "^ < > ^ ^ < > v > v"
print(f"For the coded message \"{coded_message}\" the real message was: {decipher_message(codex, coded_message)}")
print("="*80)

"""
Organizing Pokemon

This function takes a list of pokemons (represented by dictionaries)
and returns a new dictionary where the Pokemon names are grouped by
type. 

Parameters:
    A list of dictionaries representing pokemons.
    Example of the pokemon dictionary:
    {
        "name": "Pikachu",
        "type": "Electric"
    }
Returns:
    A Dictionary that groups Pokemons by type. 
    Example of the dictionary:
    {
        "Electric": ["Pikachu", "Emolga", "Voltorb"],
        "Fire": ["Charizard", "Magmar"],
        "Dark": ["Darkrai"]
    }
"""
def groupByType(pokemonList: list) ->dict:
    pass

# Tester
pokemon1 = [{"name": "Charizard", "type": "Fire"}, 
            {"name":"Squirtle", "type": "Water"},
            {"name": "Bulbasaur", "type": "Grass"}
            ]
print(groupByType(pokemon1))
print()

pokemon1 = [{"name": "Magmar", "type": "Fire"}, 
            {"name":"Raichu", "type": "Electric"},
            {"name": "Pikachu", "type": "Electric"},
            {"name": "Charizard", "type": "Fire"}, 
            {"name":"Tentacool", "type": "Water"},
            {"name": "Oddish", "type": "Grass"},
            {"name": "Houndour", "type": "Fire"}, 
            {"name":"Magikarp", "type": "Water"},
            {"name": "Venusaur", "type": "Grass"}
            ]
print(groupByType(pokemon1))
print("="*80)

"""
Actually Working
This function receives 3 sets:
- employees: All employees in a factory
- out_sick: All the employees that are out sick
- on_vacation: All the employees that are on vacation

Return a new set with all the employees that are currently 
working in the factory (not out sick or on vacation)
"""
def working_employees(employees: set, out_sick: set, on_vacation: set):
    pass

employees = {"John", "Mary", "Bill", "Jenny", 
             "Harry", "Emily", "Ken", "Jordan", "Lizzy", "Mike"}
out_sick = {"John", "Ken", "Jenny"}
on_vacation = {"Bill", "Jordan"}
print(working_employees(employees, out_sick, on_vacation))


"""
Upper count
Count how many uppercase characters are in a string 
RECURSIVELY.
"""
def upper_count(string: str) -> int:
    pass

# Tester
text1 = "Hello, WorlD!"
print(f"For {text1}: {upper_count(text1)} (expected: 3)")
print()

text1 = "no upper case here"
print(f"For {text1}: {upper_count(text1)} (expected: 0)")
print("="*80)

"""
Find max even

Find the largest even number in the list RECURSIVELY.
If there are no even values return 0

Remember you can use helper functions if that's easier
"""
def largest_even(values: list)->int:
    pass

values1 = [3, 8, 11, 2, 6]
print(f"For values {values1}: {largest_even(values1)} (expected: 8)")
print()

values1 = [-10, -3, -4, -8]
print(f"For values {values1}: {largest_even(values1)} (expected: -4)")
print("="*80)
"""
Replace (RECURSIVE)
Write a funtion that receives a string and returns a new string that 
replaces all whitespace for '_' from the given string. 
"""
def replace_spaces(string: str)-> None:
    pass

text1 = "Hello  world from Python"
print(f"For {text1}: {replace_spaces(text1)} (expected: 'Hello__world_from_Python')")
print()

text1 = ""
print(f"For {text1}: {replace_spaces(text1)} (expected: '')")
print("="*80)
"""
Moving through Map (RECURSIVE)
Receives a list of movements, a starting position (a list of 2 values), and a map (2D list)
Starting at position 0, 0 of the list use the list of 
movements to move through the map recursively.
Return the value at the final position.

If you reach a dead end (try to move to an invalid position) return -1

Movements are to be interpreted as follows: 
 ^ UP: Move one row up (0, -1)
 v DOWN: Move one row down (0, +1)
 > RIGHT: Move one column to the left (+1, 0)
 < LEFT: Move one column to the right (-1, 0)

Remember: Origin (0, 0) is the top left corner

Starting position is a list: (x, y), where x is the row and y the column
"""
def move_through_map(movements:list, start:list, map:list[list]):
    pass

# Tester
map1 = [[1, 22, 3, 12, 56, 90],
        [6, 55, 48, 34, 81, 99],
        [17, 68, 39, 12, 65, 34]]
movements1 = ['>', '>', 'v', 'v', '<']
print(f"For movements {movements1} starting at [0, 0]: {move_through_map(movements1, [0, 0], map1)} (expected: 68)")
print()

movements1 = ['<', 'v', '>', '^', '^', '^']
print(f"For movements {movements1} starting at [2, 1]: {move_through_map(movements1, [2, 1], map1)} (expected: -1)")
print("="*80)
