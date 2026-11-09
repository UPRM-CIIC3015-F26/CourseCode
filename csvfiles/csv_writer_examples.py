import csv

def csv_writer():
    with open("csvfiles/standings.csv", "w") as f:
        file_writer = csv.writer(f)

        file_writer.writerow(["Team", "Wins", "Losses"])
        file_writer.writerow(["Gigantes de Carolina", 4, 1])
        file_writer.writerow(["Criollos de Caguas", 2, 1])
        file_writer.writerow(["Cangrejeros de Santurce", 3, 2])


def csv_writer_append():
    with open("csvfiles/standings.csv", "a") as f:
            file_writer = csv.writer(f)

            file_writer.writerow(["Leones de Ponce", 2, 3])
            file_writer.writerow(["Senadores de San Juan", 1, 2])
            file_writer.writerow(["Indios de Mayaguez", 1, 4])

csv_writer()
csv_writer_append()