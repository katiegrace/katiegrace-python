import turtle as t
import random

pen = t.Pen()
t.setup(width = 700, height = 700)


def part1() :
    pen.setpos(0, 0)
    t.forward(100)  # line
    print("done with line")
    pen.penup()
    pen.setpos(0, 0)
    pen.pendown()
    t.reset()

    for x in range(4):  # square
        pen.pencolor("#22da4c")
        pen.forward(200)
        pen.left(90)
    print("done with square")
    pen.penup()
    pen.setpos(0, 0)
    pen.pendown()
    pen.reset()

# t.left(90)
# for x in range(360) :
#     t.forward(1)
#     t.right(1)
# t.right(90)
# t.forward(300)

    t.color("red")
    t.circle(300, 360)  # circle
    print("done with circle")
    pen.penup()
    pen.setpos(0, 0)
    pen.pendown()
    pen.reset()

    aColor = (0.2, 0.8, 0.99)
    t.color(aColor)
    t.forward(400)
    t.left(120)
    t.forward(400)
    t.left(120)
    t.forward(400)
    print("done with triangle")
    t.reset()

def part2() :
    askColor = input("What color do you want to draw with? (black, red, blue, green)")
    askLength = input("What length do you want the sides to be?")
    askSides = input("How many sides do you want?")
    if int(askSides) <= 2 or int(askLength) == 0 :
        print("this doesn't work")
        return
    angle = 360 / int(askSides)
    pen.penup()
    pen.setpos(200, 200)
    pen.pendown()
    pen.circle(50, 360)

    for x in range(0, int(askSides)) :
        t.color(str(askColor))
        t.forward(int(askLength))
        t.left(angle)


def part3() :
    pen.color("red")
    pen.penup()
    pen.setpos(100, 100)
    pen.pendown()
    pen.circle(50, 360)
    pen.penup()
    pen.setpos(150, -150)
    pen.pendown()
    pen.color("blue")
    for x in range(4):  # square
        pen.forward(50)
        pen.left(90)
    pen.penup()
    pen.setpos(-150, -150)
    pen.pendown()
    pen.color("green")
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.left(120)
    pen.forward(50)
    pen.penup()
    pen.setpos(-150, 150)
    pen.pendown()
    pen.color("pink")
    for x in range(2) :
        pen.forward(60)
        pen.left(90)
        pen.forward(30)
        pen.left(90)


def part4() :
    pen.speed(20)
    angle = 10
    for x in range(int(360/angle)) :
        pen.pencolor("coral")
        pen.circle(100)
        pen.left(angle)
    for x in range(int(360/angle)) :
        pen.pencolor("#f442d1")
        pen.circle(75)
        pen.left(angle)
    for x in range(int(360/angle)) :
        pen.pencolor("#45f9f3")
        pen.circle(40)
        pen.left(angle)




# part1()
# part2()
# part3()
part4()

t.exitonclick()
