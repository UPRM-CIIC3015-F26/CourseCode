a = [10, 6, 20, 30]
b = [0] * 4
empty = []

# Print Lists
def print_list(seq):
    print(seq)

print("Print List")
print_list(a)

# Iterate While

def iterate_while(seq):
    index = 0
    while index < len(seq):
        print(seq[index])
        index +=1

print("Iterate While")
iterate_while(a)
# Iterate For Range

def iterate_range(seq):
    for i in range(len(seq)):
        print(f"Posicion:{i}, value:{seq[i]}")

print("Iterate Range:")
iterate_range(a)

# Iterate for Loop
def iterate_for(seq):
    for item in seq:
        print(item)
print("Just For:")
iterate_for(a)
