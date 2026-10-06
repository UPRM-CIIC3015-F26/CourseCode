# How do we count
def count(num):
    i = 1
    while i <= num:
        print(i)
        i += 1
# count(10)  

# What if we wanted to count backwards?
def count_backwards(n):
    while n > 0: # n >= 1
        print(n)
        n -= 1 # n = n -1
# count_backwards(7)

# What happens if the condition is wrong?
def bad_loop():
    i = 12
    while i > 10:
        print(i)
        i -= 1

bad_loop()