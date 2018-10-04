for i in range(1, 6) :
    added = int(i) + 10
    print(str(i)+ " + 10 = " + str(added))
    mult = int(i) * 10
    print(str(i) + " * 10 = " + str(mult))

thisList = [10, 20, 30 , 40, 50]
print(thisList)

for x in thisList :
    for y in range(0, len(thisList)) :
        thisList[y] = int(x) * 10
    print(thisList)




