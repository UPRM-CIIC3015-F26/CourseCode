cost = float(input("What does it cost? "))

if cost < 30:
    print("This is really cheap!")
elif cost < 50:  #cost >= 30 and cost < 50:
    print("This is OK")
elif cost < 90: #cost >= 50 and cost < 90
    print("This is not ok....")
else:
    print("STOP!")