"""
Make a function called exponential, that receives:
 - num
 - exp
 This function returns the result of num^exp.

 DO IT ITERATIVELY! (This means use loops)
"""
def exponential(num, exp):
    res = 1 # result
    i = 1  # count
    while i <= exp:
        res *= num
        i += 1
    return res

print(exponential(2, 4))
print(2**4)