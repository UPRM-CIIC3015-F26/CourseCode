a = [0,10,10,20,30]

b = [5, 15, 25, 35]

# Find 10, 11
print(a.index(10))
# print(a.index(11))


#  Add at the end
a.append(35)
print(a)

# Extend Mutation/No Mutation
a.extend([1,7])
print(a)

# Sort Mutation Not Mution
a.sort()
print(a)
print(sorted(a))
# Max/Min/Sum
print(max(a))
print(min(a))
print(sum(a))

# Remove (Pop, remove, del)
z = a.pop()
print(f"removed:{z} now: {a}")
a.remove(10)
print(f"removed 10 {a}")
# Modify in Place
a[0] = 1
print(a)


# Create list from 0 to 9
r = []
for i in range(10):
    r.append(i)

print(r)