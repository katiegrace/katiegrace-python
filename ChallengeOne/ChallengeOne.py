newList = [1, 2, 3, 4]
newList1 = [1, 2, 3, 4]
print(newList)
mult = input("What number do you want to multiply your list by? ")
mult1 = input("What's another number you want to multiply your list by? ")


def multiply(list, multi) :

    times1 = (list[0] * int(multi))
    times2 = (list[1] * int(multi))
    times3 = (list[2] * int(multi))
    times4 = (list[3] * int(multi))

    newNewList = [times1, times2, times3, times4]
    return(newNewList)


result = (multiply(newList, mult))
print(result)

result = (multiply(result, mult1))
print(result)



