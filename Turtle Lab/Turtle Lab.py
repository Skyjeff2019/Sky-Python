import turtle as t

t.bgcolor("yellow")

t.setup(width=750, height=750)

pen = t.Pen()
pen.speed(200)

black = (0.0, 0.0, 0.0)
white = (1.0, 1.0, 1.0)
red = (1.0, 0.0, 0.0)
green = (0.0, 1.0, 0.0)
blue = (0.0, 0.0, 1.0)


def basicL():
    moveTo(-50, 0)
    pen.forward(100)

#The origin on the screen should be (0,0)

def basicS():
    pen.pencolor(red)
    moveTo(-100, -100)
    for x in range(4):
        pen.forward(200)
        pen.left(90)


def basicC():
    pen.pencolor(blue)
    moveTo(0, -300)
    pen.circle(300)

def basicT():
    pen.pencolor('#33cc8c')
    moveTo(-200, -150)
    for x in range(3):
        pen.forward(400)
        pen.left(120)



def moveTo(x, y):
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()

#don't forget to call the functions

basicL()
basicS()
basicC()
basicT()

t.exitonclick()
