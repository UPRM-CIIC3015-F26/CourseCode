def ask_for_password():
    password = ""
    while password != "1234":
        password = input("Password?")

        if password == '1234':
            print("Access Granted!")
        else:
            print("Wrong password! >:(")

ask_for_password()