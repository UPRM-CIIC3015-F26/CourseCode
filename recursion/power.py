# This calculates n**exp (n^exp)
# 3^4 = 3*3*3*3 = 3 * 3^3 
# 3^3 = 3 * 3^2
# N^exp = N * N^(exp -1)
def power(n, exp):
    if exp == 0:
        return 1
    return n * power(n, exp - 1)

print(f"3^2 = {power(3, 2)}")
print(f"2^4 = {power(2, 4)}")
print(f"10^5 = {power(10, 5)}")

