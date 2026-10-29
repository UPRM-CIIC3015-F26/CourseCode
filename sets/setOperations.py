physics_students = {"John", "Mary", "Jil", "Ben"}
calculus_students = {"Ken", "Joe", "Jil", "Ben", "Zeke"}
biology_students = {"John", "Ben", "Michael", "Jim"}

# Find students taking both Physics and calculus
print(physics_students.intersection(calculus_students))

# Find all students taking all three course
print(physics_students.intersection(biology_students).intersection(calculus_students))

# Find students taking biology, but not calculus
print(biology_students.difference(calculus_students))

# Find all the students enrolled in university
set1 = physics_students.union(biology_students)
print(set1.union(calculus_students))

set1 = {1, 2, 3, 4}
set2 = {1, 2, 3, 4}
# How do I check if two sets are identical using there funtions
print(len(set1.difference(set2)) == 0 and len(set2.difference(set1)) == 0)