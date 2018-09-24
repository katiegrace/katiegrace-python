def main() :
    gradeLev = input("What grade are you in? ")

    gradeLevelNum = int(gradeLev)
    print(yearInSchool(gradeLevelNum))

    classGrades = [92.5, 88.6, 77.2, 99.7]
    numberOfClassGrades = (len(classGrades))
    print(numberOfClassGrades)
    numGrade = (getAverageGrade(classGrades, numberOfClassGrades))

    letterGrade = (getLetterGrade(numGrade))
    print(letterGrade)

    if letterGrade == "A" or "A-" or "B+" or "B" or "B-" or "C+" or "C" or "C-" :
        print("Congratulations you are passing! ")
    else :
        print("You better get to work - you are failing! ")




def yearInSchool(level) :
    if level == 12 :
        return "Senior "
    elif level == 11 :
        return "Junior "
    elif level == 10 :
        return "Sophomore "
    elif level == 9 :
        return "Freshman "
    else :
        return "You aren't in high school! "

def getAverageGrade(grades, length1) :
    added = grades[0] + grades[1] + grades[2] + grades[3]
    average = (added / length1)
    return float(average)

def getLetterGrade(number) :
    if number >= 92.5 :
        return "A"
    elif number >= 90.5 :
        return "A-"
    elif number >= 88.5 :
        return "B+"
    elif number >= 83.5 :
        return "B"
    elif number >= 81.5 :
        return "B-"
    elif number >= 79.5 :
        return "C+"
    elif number >= 74.5 :
        return "C"
    elif number >= 72.5 :
        return "C-"
    elif number >= 70.5 :
        return "C-"
    elif number >= 65.5 :
        return "D"
    else :
        return "F"

main()

