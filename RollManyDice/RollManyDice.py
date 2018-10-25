def main() :
    count = 0
    print(defineDice(count))
    play = "Y"
    count = count + 1

    while(play) :
        randomNum = random()
        print("Random number is: " + str(randomNum))
        print("count = " + str(count))
        print(defineDice(randomNum))
        count = int(count) + 1
        play = input("Play again? Y or N   ") == "Y"

    print("You've played " + str(count) + " times")


def defineDice(number) :  # number = count
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

    for dice in everyDie :
        for i in dice :
            print(i)
    # if number == 0 :
    #     print(everyDie[0])    # printing each dice
    #     print(everyDie[1])
    #     print(everyDie[2])
    #     print(everyDie[3])
    #     print(everyDie[4])
    #     print(everyDie[5])
    #
    # if int(number) == 1 :
    #     return(everyDie[0])
    # elif int(number) == 2:
    #     return(everyDie[1])
    # elif int(number) == 3:
    #     return(everyDie[2])
    # elif int(number) == 4:
    #     return(everyDie[3])
    # elif int(number) == 5:
    #     return(everyDie[4])
    # elif int(number == 6) :
    #     return(everyDie[5])
    # else:
    #     print("")


def random() :
    import random
    for x in range(7) :
        anInt = random.randint(1, 6)
    return anInt

main()
