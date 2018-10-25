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
    topAndBottom = "  ------- \n"  # making different combinations
    onLeft = " | *     | \n"
    onRight = " |     * | \n"
    middleStar = " |   *   | \n"
    twoStars = " | *   * | \n"
    noStars = " |       | \n"
    diceForOne = topAndBottom + noStars + middleStar + noStars + topAndBottom   # putting combinations together
    diceForTwo = topAndBottom + noStars + twoStars + noStars + topAndBottom
    diceForThree = topAndBottom + onLeft + middleStar + onRight + topAndBottom
    diceForFour = topAndBottom + twoStars + noStars + twoStars + topAndBottom
    diceForFive = topAndBottom + twoStars + middleStar + twoStars + topAndBottom
    diceForSix = topAndBottom + twoStars +twoStars + twoStars + topAndBottom
    if number == 0 :
        print(diceForOne)    # printing each dice
        print(diceForTwo)
        print(diceForThree)
        print(diceForFour)
        print(diceForFive)
        print(diceForSix)

    if int(number) == 1 :
        return(diceForOne)
    elif int(number) == 2:
        return(diceForTwo)
    elif int(number) == 3:
        return(diceForThree)
    elif int(number) == 4:
        return(diceForFour)
    elif int(number) == 5:
        return(diceForFive)
    elif int(number == 6) :
        return(diceForSix)
    else:
        print("")


def random() :
    import random
    for x in range(7) :
        anInt = random.randint(1, 6)
    return anInt

main()
