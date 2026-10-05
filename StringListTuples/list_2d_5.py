import random

def gen_random_int_matrix(rows, cols, max):
    result = []
    next_int = 0
    for i in range(rows):
        next_row = []
        for j in range(cols):
            next_row.append(random.randint(0, max))
            next_int += 1
        result.append(next_row)
    return result

def gen_sequential_int_matrix(rows, cols):
    result = []
    next_int = 0
    for i in range(rows):
        next_row = []
        for j in range(cols):
            next_row.append(next_int)
            next_int += 1
        result.append(next_row)
    return result

def pretty_print(matrix):
    print("[")
    for i in range(len(matrix)):
        print(matrix[i], ",")
    print("]")

def transpose(matrix):
    # Assumes all rows have same length
    result = []
    for col in range(len(matrix[0])):
        next_row = []
        for row in range(len(matrix)):
            next_row.append(matrix[row][col])
        result.append(next_row)
    return result

def horizontal_flip(matrix):
    result = []
    for row in range(len(matrix)):
        next_row = []
        for col in range(len(matrix[row])-1,-1,-1):
            next_row.append(matrix[row][col])
        result.append(next_row)
    return result

print(gen_random_int_matrix(4,3, 100))

original_matrix = gen_random_int_matrix(4,3,100)
print("Original Matrix:")
pretty_print(original_matrix)
print("Transposed Matrix:")
pretty_print(transpose(original_matrix))
print("Horizontally Flipped Matrix:")
pretty_print(horizontal_flip(original_matrix))