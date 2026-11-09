import csv


def print_all_rows():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.reader(f)
        
        for row in contents:
            print(row)


def print_cell():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.reader(f)
    
        for row in contents:
            print(row[1])



def restock_check():
    restock_list = []    

    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.reader(f)

        next(contents)
        
        for row in contents:
            if int(row[2]) <= int(row[3]):
                restock_list.append(row)

    return restock_list


def cleanup_data():
    with open("csvfiles/pepper_inventory.csv", "r") as f:
        contents = csv.reader(f)

        next(contents)
    
        for row in contents:
            if "#P" not in row[0]:
                print("Plant without pepper code in inventory.")
                print(f"Check row {row}.")

#print_all_rows()

#print_cell()

#print(restock_check())

#cleanup_data()