# Would you like to by premium? Yes/y?
ask = input("Do you want premium?")
ask = ask.upper()
if ask == "YES" or ask == 'Y':
    print("You now have premium!!!!")
else:
    print("No premium >:(")