def has_duplicates(values):
    set1 = set()
    for x in values:
        set1.add(x)
    return len(values) != len(set1)
animals = ["cat", "dog", "bird"]
if has_duplicates(animals):
    print("The list has duplicates.")
else:
    print("The list has no duplicates.")