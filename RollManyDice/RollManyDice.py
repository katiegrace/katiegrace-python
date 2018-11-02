import random
DICE_NUM = 98

def main() :

    # count = count + 1
    newDiceList = [0] * 6
    newDiceList = defineDice()

    printSideBySide(newDiceList)

    count = 0
    play = "Y"

    while(play) :
        randomNum = random1()
        # print("Random number is: " + str(randomNum))
        print("count = " + str(count))

        anotherDice = [0] * DICE_NUM
        roll = 0

        for num in range(0,DICE_NUM) :
            roll = random1()
            print(str(roll+1) + " rolled", end = "\t")

            anotherDice[num] = newDiceList[roll]

        print()
        printSideBySide(anotherDice)

        count = int(count) + 1

        play = input("Play again? Y or N   ") == "Y"


    print("You've played " + str(count) + " times")


def defineDice() :  # number = count
    diceList2 = [0] * 6
    topAndBottom = "  ------- "  # making different combinations
    onLeft = " | *     | "
    onRight = " |     * | "
    middleStar = " |   *   | "
    twoStars = " | *   * | "
    noStars = " |       | "
    diceOne = [topAndBottom, noStars, middleStar, noStars, topAndBottom]
    diceTwo = [topAndBottom, noStars, twoStars, noStars, topAndBottom]
    diceThree = [topAndBottom, onLeft, middleStar, onRight, topAndBottom]
    diceFour = [topAndBottom, twoStars, noStars, twoStars, topAndBottom]
    diceFive = [topAndBottom, twoStars, middleStar, twoStars, topAndBottom]
    diceSix = [topAndBottom, twoStars, twoStars, twoStars, topAndBottom]
    everyDie = [diceOne, diceTwo, diceThree, diceFour, diceFive, diceSix]
    diceNewList = []
    randomNumber = random1()

    # for dice in everyDie :
    #     for i in dice :
    #         print(i)

    for aNum in range(0, 6) :
        if aNum == 0 :
            diceList2[aNum] = everyDie[0]
        elif aNum == 1 :
            diceList2[aNum] = everyDie[1]
        elif aNum == 2 :
            diceList2[aNum] = everyDie[2]
        elif aNum == 3 :
            diceList2[aNum] = everyDie[3]
        elif aNum == 4 :
            diceList2[aNum] = everyDie[4]
        elif aNum == 5 :
            diceList2[aNum] = everyDie[5]
    return(diceList2)

def printSideBySide(diceNewList) :
    for row in range(0, len(diceNewList[0])) :
        for col in range (0, len(diceNewList)) :
            print(diceNewList[col][row], end = "\t")
        print()


def random1() :
    anInt = random.randint(0, 5)
    return anInt

main()
