def stop_at(stop = 5):
    i = 1
    while i < stop:
        print(i)
    
def skip_if_divisible_by(div = 5):
    i = 1
    while i < 20:
        if(i % div == 0):
            continue
        print(i)
