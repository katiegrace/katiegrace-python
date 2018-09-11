print("What is your grade? ")
numGrade = int(input())
print(numGrade)

if numGrade >= 90:
    print("Yahoo you got an A! ")

elif numGrade >= 80:
        print("Good you got a B!")

elif numGrade >= 70:
        print("Okay you got a C! ")
else:
    print("You better study harder ")



print("What is your favorite color? ")
userInput = input()
print("You said " + userInput)

if userInput == "blue":
    print("The sky is blue ")

elif userInput == "green":
        print("The forest is green ")

elif userInput == "red":
        print("I love red ")

elif userInput == "yellow":
    print("Yuck yellow ")

else:
    print("I am a dumb computer - I only know 4 colors ")
