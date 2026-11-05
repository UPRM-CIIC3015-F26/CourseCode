

def write_ingredients():
    with open("ingredients.txt", "w") as f:
        f.write("flour\n")
        f.write("sugar\n")
        f.write("eggs\n")
        f.write("butter\n")

    with open("ingredients.txt", "r") as f:
        contents = f.read()
        print(contents)


def configurations():
    with open("configurations.txt", "w") as f:
        f.write("volume = 75\n")
        f.write("shuffle = no\n")
        f.write("fadein = 0\n")
        f.write("fadeout = 0\n")

    with open("configurations.txt", "a") as f:
        f.write("crossfade = 5\n")

    # Review the file contents
    with open("configurations.txt", "r") as f:
        contents = f.read()
        print(contents)


def update_game_status(filename, level, score):
    with open(filename, "a") as f:
        f.write(f"Level: {level}\n")
        f.write(f"Score: {score}\n")


def do_update():
    update_game_status("player5.txt", 1, 70)
    update_game_status("player5.txt", 2, 120)
    update_game_status("player5.txt", 3, 186)

    # Review the file contents
    with open("player5.txt", "r") as f:
        contents = f.read()
        print(contents)

#write_ingredients()
# configurations()
do_update()