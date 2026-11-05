filename = "daily_sightings.txt"

# Open Traditional
f = open(filename, "r")
print(f.read())
f.close()

# With and Read
with open(filename, "r") as f:
    print(f.read())

# With and ReadLine
with open(filename, "r") as f:
    print(f.readline())


# With and Readlines
with open(filename, "r") as f:
    print(f.readlines())



# For loops
with open(filename, "r") as f:
    for line in f:
        print(line)
