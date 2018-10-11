def main() :
    oneSide = input("What do you want the length and width to be (same)? ")
    makeSquare(oneSide)


def makeSquare(side) :
    for x in range(0, int(side)) :
        for i in int(side) :
            print("*")

main()
