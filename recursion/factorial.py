# Factorial iterative
def factorial(n):
    res = 1
    for x in range(1, n+1):
        res *= x
    return res

# Factorial but recursive
def recFactorial(n):
    if n == 1 or n == 0:
        return 1
    return n * recFactorial(n -1)

# print(f"5! = {factorial(5)}")
# print(f"1! = {factorial(1)}")
# print(f"3! = {factorial(3)}")
# print(f"0! = {factorial(0)}")
print(f"5! = {recFactorial(5)}")
print(f"1! = {recFactorial(1)}")
print(f"3! = {recFactorial(3)}")
print(f"0! = {recFactorial(0)}")
