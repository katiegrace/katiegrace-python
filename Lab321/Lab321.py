def main() :
    gradeLev = input("What grade are you in? ")

    gradeLevelNum = int(gradeLev)
    print(yearInSchool(gradeLevelNum))  # prints year in school (the long way)

    classGrades = []
    nums = input("How many classes do you take? ")
    for i in range(0, int(nums)) :
        question = int(input("Grade of class " + str(i + 1) + ": "))
        classGrades.append(question)
    numberOfClassGrades = (len(classGrades))
    print(str(numberOfClassGrades) + " classes")
    numGrade = (getAverageGrade(classGrades)) # puts average grade into a variable
    print(numGrade)

    letterGrade = (getLetterGrade(numGrade))
    print(letterGrade)  # prints letter grade

    # if letterGrade == "A" or "A-" or "B+" or "B" or "B-" or "C+" or "C" or "C-" :
      #  print("Congratulations you are passing! ")
    # elif letterGrade == "D+" or "D" or "D-" or "F" :
      #  print("You better get to work - you are failing! ")
   #  else :
       # print("You better get to work - you are failing! ")  # prints whether passing/failing based on GPA
    if letterGrade == 'F' :
        print("You better get to work - you are failing! ")
    else :
        print("Congratulations you are passing! ")



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
        return "You aren't in high school! "  # determines grade level and returns it

def getAverageGrade(grades) :
    newGrades = grades
    lengthOfList = (float(len(newGrades)))
    add1 = 0.0
    for x in newGrades :
        add1 = float(add1) + int(x)
    # added = grades[0] + grades[1] + grades[2] + grades[3]
    average = (float(add1) / int(lengthOfList))
    return float(average)  # calculates average grade

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
        return "F"  # determines the letter grade

main()  # runs code

