
import turtle as t

pen = t.Pen()
t.setup(width = 600, height = 500)

def drawing1(angle):
    t.bgcolor("black")
    pen.pencolor("#faa063")
    pen.pensize(50)
    for x in range(4):
        pen.forward(50)
        pen.left(angle)


def drawing2(angle) :
    pen.pencolor("#42f4d9")
    for x in range(4):
        pen.forward(50)
        pen.left(angle)

drawing1(90)
pen.penup()
pen.setpos(100, 100)
pen.pendown()
drawing2(90)
pen.penup()
pen.setpos(-100, -100)
pen.pendown()


def drawing3(angle) :
    pen.pencolor("#22da4c")
    for x in range(4) :
        pen.forward(60)
        pen.left(angle)
        pen.forward(30)
        pen.left(angle)

def drawing4(angle) :
    pen.pencolor("#da38ff")
    for x in range(4) :
        pen.forward(60)
        pen.left(angle)
        pen.forward(30)
        pen.left(angle)

drawing3(90)
pen.penup()
pen.setpos(-200, -200)
pen.pendown()
drawing4(90)
pen.penup()
pen.setpos(200, 200)
pen.pendown()




# Additional Turtle Info
#
# Specify a screen size and/or start position
#turtle.setup(width=600, height=500)

# Moving the pen
#
# turtle.forward(10)
# turtle.backward(10)
# turtle.left(10)
# turtle.right(10)
# turtle.setx(10)
# turtle.sety(10)
# turtle.goto(10, 10)
# turtle.setpos(10, 10) # same as goto()

# Move the arrow/turtle back to the beginning (origin)
# turtle.home()

# Clear the screen and return to the origin
# turtle.reset()

# Hide/show the arrow (turtle) while printing
# turtle.hideturtle()# turtle.showturtle()

# Set drawing animation) speed; 0 means no animation
# turtle.setspeed(0)

# Get screen size info
# turtle.window_height()
# turtle.window_width()

# Set a title
# turtle.title("My Drawing")

# Finish with this - it tells Turtle to pause until
# you close.  Otherwise, it'd just draw your image then quit.
t.exitonclick()

#
# ToDos: (You can use the documentation below for the following)
#
# 1) Use a different background color for the screen.  Try red, blue and black.
# 2) Draw a 2 squares and 2 rectangle.
# 2a) Make one of each filled and one 'empty' or not filled.
# 2b) Use different colors for the fill and border or lines

#
# Documentation
# Turtle Graphics - https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

#
# Geek-down on color:  ¯\_(ツ)_/¯
#
# There are several different systems for creating colors
# RGB and RGBA are probably the most popular.  You've already seen
# RGB - RGBA just adds another variable for alpha (A) or transparency
# Even within RGB/RGBA there are options - some sytems encode the color
# as number up to 256 (CHAR datatype in some languages like Java).
# And some encode the color as a decimal number between 0.0 and 1.0
# And actually, Turtle can handle either encoding.
# Hex or Hexadecimal (which means 16 or base 16) is very popular in web development and HTML/CSS.

# A Hex color usually looks something like: #ffe063
# The hash or # sign indicates its a hexadecimal number.
# Remember when I said some RGB systems use a number between 0 and 255 (256 range)?
# Actually, hex colors are RGB colors.
# Hex numbers are base 16 (vs base 10 in decimal).  We don't want
# 2 digits in the number.  So how do we represent numbers greater than 9?
# With letters.  In hex - 0 - 9 are just like and have the same value
# as decimal -- and the numbers 10 - 15 (there is no 16 because it starts at 0
# and goes to 15 for a range of 16 -- like decimal goes from 0 to 9) start at 'a' or 'A'
# and go to 'f' or 'F' for 15.  ('A' = 10; 'B' = 11; ... 'F' = 15)
#
# Looking at the hex color above - like decimal -- every place is a power of the base number - 16 in this case.
# And the number is arranged in pairs of digits. And its basically an RGB value.
# ff = red part; e0 = green part; 63 = blue part
# Now that we know hoe to decode hex, we can convert these to their decimal parts.
# ff = (15 * 16^1) + (15 * 16^0) = 240 + 15 = 255 -- which is the highest number in the integer scale
# e0 = (14 * 16^1) + (0 * 16^1) = 224 + 0 = 224
# 63 = (6 * 16^1) + (3 * 16^0) = 96 + 3 = 99
# So, the hex color #ffe063 = (255, 224, 99) in standard RGB
# There are lots of color converters on the web you can use to experiment with this.

# We won't go too much into color theory in this class, but just understand its a very rich topic
# and there are other colors schemes used in digital printing, photography, Home Depot paint colors, etc...
# Each one with a different strength.  Why so many, because real color in the world is much broader
# than we humans can see or appreciate.  Colors go further into the electro-magnetic spectrum than humans can
# see.  So any system that codes colors for humans is going to have trade-offs.
# And different color encodings have been created to do different jobs.
# RGB / RGBA is by far the most popular in general computing.
#
# But there others that you might come across such as:  HSL (hue, saturation and luminosity or lightness) and
# CMYK (cyan, magenta, yellow and key).
#
# The only other thing to know is that color systems can also be classified as additive or subtractive.
# As the names imply, in an additive system -- you add color into to form the color and in subtractive you subtract.
# Computers and monitors and tv's are examples of additive color.  So RGB is an additive scheme.
# CMYK is an example of a subtractive system and is widely used in the print industry.  Usually 'real-world' colors,
# like paint and ink are subtractive and virtual or computer systems are additive.
#
# How many colors could we create with the 256 type RGB scheme?
# 256^3 = 256 * 256 * 256 = 16,777,216 colors!
