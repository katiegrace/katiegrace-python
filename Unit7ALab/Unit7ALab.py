class Pet() :
    petType = "cage free pet"

    def __init__(self, pType, pName, pBreed):
        self.type = pType
        self.name = pName
        self.breed = pBreed

    def whatIsIt(self):
        return(str("The type of pet the is: " + self.type + ". The name is: " + self.name + ". The breed is: " + self.breed + "."))

class Cage() :
    petType = "caged pet"

    def __init__(self, cType, cDanger):
        self.type = cType
        self.danger = cDanger

    def whatDanger(self):
        if(self.danger == "True"):
            return("The animal is dangerous.")
        elif(self.danger == "False"):
            return("The animal is not dangerous.")

def main() :
    myPet1 = Pet("Dog", "Luna", "Golden Doodle")

    print(myPet1.whatIsIt())
    print(myPet1.name)

    myPet2 = Pet("Cat", "Sally", "Maine Coon")

    print(myPet2.whatIsIt())

    myCage1 = Cage("Snake", "True")

    print(str("The animal is: " + myCage1.petType + ". The type of animal is a: " + myCage1.type + ". " + myCage1.whatDanger()))

    myCage2 = Cage("Rat", "False")

    print(str("The animal is: " + myCage2.petType + ". The type of animal is a: " + myCage2.type + ". " + myCage2.whatDanger()))

main()
