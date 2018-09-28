def main() :
    ask = input("Enter a word. ")
    print(ask)
    print('Your word without vowels: ' + deVowel(ask))

def deVowel(word) :
    newWord = ''
    for letter in word :
        if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter !='u' :
            newWord = newWord + letter
    return newWord

main()
