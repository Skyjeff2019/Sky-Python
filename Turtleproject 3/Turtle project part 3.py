import turtle as t

def main():
    t.title("Mo Bamba")
    t.bgcolor("blue")
    t.setup(width=800, height=800)
    t.speed(0)
    circle()
    square()
    triangle()
    rectangle()
    t.exitonclick()

def square():
    t.pencolor("red")
    moveT(100, 100)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

def circle():
    t.pencolor("yellow")
    moveT(-100, -300)
    t.circle(60)

def triangle():
    t.pencolor("black")
    moveT(200, -125)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)

def rectangle():
    t.pencolor("orange")
    moveT(-300, 150)
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(150)

def moveT(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()

main()
