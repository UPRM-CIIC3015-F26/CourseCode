age = 19
hasID = True
# To gain access a person must be 18 and have an ID
print(f"The person is {age} years old and has ID? {hasID}")
print("Can enter:", (age >= 18) and hasID)

# To gain access the person must be either 18 or an employee
isEmployee = False
print("Can enter:",(age >= 18) or isEmployee)

# To gain access the person must be an Employee or must be 18 and have an ID
print(f"Age: {age}, ID: {hasID}, isEmployee: {isEmployee}")
print(((age >=18) and hasID) or isEmployee)