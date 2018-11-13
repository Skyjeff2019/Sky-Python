
# ToDos: (You can use the documentation below for the following)
#
# 1) Use a different background color for the screen.  Try red, blue and black.
# 2) Draw a 2 squares and 2 rectangle.
# 2a) Make one of each filled and one 'empty' or not filled.
# 2b) Use different colors for the fill and border or lines



import turtle as t

def alltogether():
    squaredrawing()
    sqauredrawingv2()
    rectangle()
    rectranglev2()

def squaredrawing():
    t.bgcolor("blue")
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

def sqauredrawingv2():
    t.penup()
    t.forward(100)
    t.pendown()
    t.pencolor("red")
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

def rectangle():
    t.penup()
    t.backward(250)
    t.pendown()
    t.pencolor("black")
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

def rectranglev2():
    t.penup()
    t.backward(150)
    t.pendown()
    t.pencolor("yellow")
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)

alltogether()
