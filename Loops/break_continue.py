def stop_at(stop = 5):
    i = 0
    while i < 20:
        i += 1
        print(i)
        if i == stop:
            break
    print("Out of loop")

stop_at(7)

def skip_if_divisible_by(div = 5):
    i = 0
    while i < 10:
        i += 1
        if(i % div == 0):
            continue
        print(i)

skip_if_divisible_by()