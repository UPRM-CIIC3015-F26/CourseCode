# Basic Try Catch
try:
    data = open('exceptions/grades.csv', 'r')
    print("File Opened")
except FileNotFoundError as e:
    print("Caught Error:", e.filename)


# Multiple exceptions.
try:
    data = open('exceptions/multiple.txt', 'r')
    score = int(data.read())
except FileNotFoundError:
    print("File Missing.")
except ValueError:
    print("Data Not an Integer")



# Else statement

try:
    data = open('exceptions/hello.txt', 'r')
except FileNotFoundError:
    print("File Missing.")
else:
    print(data.read())



# Finally
try:
    file = open('exceptions/grades.csv', 'r')
except FileNotFoundError:
    print("File Missing.")
finally:
    file.close()



# Raise
def calculate_grade(score):
    if score < 0:
        raise ValueError("No negative score")
    return score / 100


calculate_grade(10)

calculate_grade(-1)
print("Hello World")