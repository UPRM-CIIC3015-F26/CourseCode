def even_or_odd(num):
    retval = ""
    if num %2 == 0:
        retval = f"{num} es Par"
    else:
        retval = f"{num} es Impar"

    # return retval


text = even_or_odd(11)

print(text)