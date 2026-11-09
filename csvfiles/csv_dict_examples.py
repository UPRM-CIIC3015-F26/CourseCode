import csv


def print_all_rows():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.DictReader(f)

        for row in contents:
            print(row)

def print_keys():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.DictReader(f)

        keys = next(contents).keys()

        print(keys)


def pepper_names():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.DictReader(f)

        pepper_descriptions = []

        for row in contents:
            pepper_descriptions.append(row["Desc"])

        pepper_descriptions = sorted(pepper_descriptions)

        return pepper_descriptions


def find_best_sellers(filename, restock_threshold):

    with open(filename, "r") as f:
        contents = csv.DictReader(f)

        best_sellers = []

        for row in contents:
            if int(row["Restock_Point"]) >= restock_threshold:
                best_sellers.append(row)

        return best_sellers

#print_all_rows()
#print_keys()
#print(pepper_names())
#print(find_best_sellers("csvfiles/pepper_inventory.csv",  25))