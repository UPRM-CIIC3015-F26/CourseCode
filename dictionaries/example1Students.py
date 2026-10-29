# dictionary for student id (int) with name (str)
students = { 
    123: "John",
    234:"Mary",
    345:"Jil"
}
# print(students)
# print(students[12])
# id with grade
grades ={123: 95.7, 234: 86.3, 345: 12.7}
# print(grades)
# Print name with grade
for id in students:
    print(f"For id {id} we have student {students[id]} they got {grades[id]} in the exam")

# Do same with a tuple as value
students = {
    123: ("John", 95.7),
    234: ("Mary", 86.3),
    345:("Jil", 12.7)
}
print(students)
student_tuple = students[123]
print(student_tuple[0])
# Seeing keys and values
print(students.keys())
print(students.values())