
def main() :

    textCodes = {'ttyl' : 'talk to you later', 'wbu' : 'what about you', 'lol' : 'laugh out loud'}

    key = input("Shortcut: ")

    while (key in textCodes) :
        print(textCodes[key])
        deleteWord(textCodes)
        modifyWord(textCodes)
    addWord(textCodes, key)
    deleteWord(textCodes)
    modifyWord(textCodes)

def addWord(list, key) :
    ask = input("Do you want to add this word? (yes or no)")    # start here
    if ask == "yes" :
        answer = input("What does this mean? ")
        list[key] = answer
        print(list)
    elif ask == "no" :
        deleteWord(list)


def deleteWord(list) :
    delete = input("Do you want to delete any words? (yes or no) ")
    if delete == "yes" :
        print(list)
        takeOut = input("Which word? ")
        del list[takeOut]
        print(list)
    elif delete != "yes" :
        print(list)
        modifyWord(list)

def modifyWord(list) :
    mod = input("Do you want to modify a word? (yes or no) ")
    if mod == "yes" :
        which = input("Which word? ")
        change = input("What do you want to change it to? ")
        list[which] = change
        print(list)
    if mod != "yes" :
        print("Ok bye")
        quit()


main()



    # add = input("Do you want to add a word? (yes or no) ")
    # if add == "yes" :
    #     answer2 = input("What does this mean? ")
    #     textCodes['key'] = answer2
    # elif add == "no" :
    #     delete2 = input("Do you want to delete any words? (yes or no) ") == "yes"
    #     if delete2 == "yes" :
    #         print(textCodes)
    #         takeOut = input("Which of these words? ")
    #         del textCodes[takeOut]
    #     elif delete2 != "yes" :
    #         print(textCodes)
    #         mod = input("Do you want to modify a word? (yes or no) ")
    #         if mod == "yes" :
    #             which = input("Which word? ")
    #             change = input("What do you want to change it to? ")
    #             textCodes[which] = change
    #         else :
    #             print("Ok bye")
    #             quit()

# ask = input("Do you want to add this word? (yes or no)")    # start here
# if ask == "yes" :
#     answer = input("What does this mean? ")
#     textCodes[key] = answer
#     print(textCodes)
# elif ask == "no" :
#     delete = input("Do you want to delete any words? (yes or no) ") == "yes"
#     if delete == "yes" :
#         print(textCodes)
#         takeOut = input("Which word? ")
#         del textCodes[takeOut]
#     elif delete != "yes" :
#         print(textCodes)
#         mod = input("Do you want to modify a word? (yes or no) ")
#         if mod == "yes" :
#             which = input("Which word? ")
#             change = input("What do you want to change it to? ")
#             textCodes[which] = change
