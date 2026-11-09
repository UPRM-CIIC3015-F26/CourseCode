import csv

with open("pepper_inventory.csv", "r") as f:
    contents = csv.DictReader(f)

    for row in contents:
        print(row)