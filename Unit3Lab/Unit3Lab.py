from random import *

def aboutMe() :
    print("I go to Bellarmine")
    print("I like Python")

aboutMe()

def moreAboutMe() :
    grade = input("What grade are you in? ")
    calc = (int(grade))
    print("You've been in school for " + str(calc) + " years. ")

moreAboutMe()

city = input("What city are you from? ")
grade = input("What grade are you in? ")

def info(myCity, myGrade) :
    print("Your city is: " + city + " You're in grade " + grade)

info(city, grade)

num1 = input("Choose any number - ")
num2 = input("Choose another number greater than the first number - ")

def numbers(x, y) :
    random = randint(int(x), int(y))
    print(random)

numbers(num1, num2)

length = input("What is the length of your box? ")
width = input("What is the width of your box? ")
height = input("What is the height of your box? ")

def box(l, w, h) :
    calc1 = (2 * (int(h) * int(w)) + 2 * (int(h) * (int(l)) + 2 * (int(w) * int(l))))
    return str(calc1)

print("The area of your box is " + box(length, width, height))

def perimeter(l, w) :
    perm = (2 * (int(l) + int(w)))
    return str(perm)

print("The perimeter of your box is " + perimeter(length, width))
