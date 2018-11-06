import random
DICE_NUM = 10  # this is a constant which is the number of dice you want side by side

def main() :  # this is the main function

    # count = count + 1
    print("All 6 dice in a row")
    newDiceList = [0] * 6
    newDiceList = defineDice()

    printSideBySide(newDiceList)  # this prints out the 6 die in a row

    count = 1
    play = "Yes"

    while(play) : # while the user is playing, this will happen
        randomNum = random1()
        # print("Random number is: " + str(randomNum))
        print("game count = " + str(count) + "\n")  # this is the game counter

        anotherDice = [0] * DICE_NUM
        roll = 0

        for num in range(0,DICE_NUM) :
            roll = random1()
            print(" " + str(roll+1) + " rolled", end = "\t")

            anotherDice[num] = newDiceList[roll]

        print()
        printSideBySide(anotherDice)   # this prints the dice side by side

        count = int(count) + 1  # this increases the count

        play = input("Do you want to play again? Type \"Yes\" or \"No\"   ") == "Yes"  # asks user if they want to play again


    print("You've played " + str(count) + " times")  # when the user stops playing, it will tell them how many times they've played


def defineDice() :  # this function creates the dice
    diceList2 = [0] * 6
    topAndBottom = "  ------- "  # making different combinations of die
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

    for aNum in range(0, 6) :  # this will append the random die
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

def printSideBySide(diceNewList) :  # this will put the random die print side by side
    for row in range(0, len(diceNewList[0])) :
        for col in range (0, len(diceNewList)) :
            print(diceNewList[col][row], end = "\t")
        print()


def random1() :  # this function will create random numbers
    anInt = random.randint(0, 5)
    return anInt

main()
