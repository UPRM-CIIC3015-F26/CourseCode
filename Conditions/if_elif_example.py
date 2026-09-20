# Discounts
age = 32
hasMembership = True
isTuesday = True
"""
A person can get a discount if they have store
membership or if they are considered seniors. 
A person is considered a senior if they are 65 or older.

Members get 15% discount and seniors get 10% discount (great store!)
If someone is both a senior and a member they get a 20% discount

If they are members and it's Tuesday say HI
"""
if hasMembership and age >=65:
    print("20%")
    if isTuesday:
        print("HI")
elif hasMembership:
    print("15%")
    if isTuesday:
        print("HI")
elif age >= 65:
    print("10%")

