def fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fib(5) = {fibonacci(5)}")
print(f"fib(3) = {fibonacci(3)}")
print(f"fib(2) = {fibonacci(2)}")
print(f"fib(1) = {fibonacci(1)}")
print(f"fib(0) = {fibonacci(0)}")
print(f"fib(9) = {fibonacci(9)}")