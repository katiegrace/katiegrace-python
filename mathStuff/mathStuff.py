def main() :
    num1 = input("Enter 1 number: ")
    num2 = input("Enter a second number: ")
    num3 = input("Enter a third number: ")
    num4 = input("Enter a final number: ")
    newList = [num1, num2, num3, num4]
    mult = input("Enter a multiplier: ")
    print(mathStuff1(newList, mult))

def mathStuff1(list, multiplier) :
    secondlist = []
    for nums in list :
        secondlist.append(int(nums) * int(multiplier))
    return secondlist
main()
