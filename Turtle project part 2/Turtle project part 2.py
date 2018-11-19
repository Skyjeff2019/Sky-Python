import turtle as t

def main () :
    t.setup(width=800 , height=800)
    t.title("Turtle Graphics part 2 by skyjeff")
    t.bgcolor("red")
    t.hideturtle()
    t.speed(0)
    inputinfo ()
    circle ()
    t.exitonclick ()

def inputinfo () :
    color = input ('Input a color to draw with - ')
    length = int(input('Input the length in pixels of each side - '))
    numsides = int(input('Input the number of sides for your polygon - '))
    if numsides<=2 :
        notenoughsides()
    something (color , length , numsides)


def something (color , length , numsides) :
    t.pencolor(color)
    t.penup()
    b = (length / -2)
    c = (length / 2)
    t.setpos(b , c)
    t.pendown ()
    a = 360 / numsides
    for x in range(0,numsides) :
        t.forward(length)
        t. right(a)

def circle () :
    t.penup()
    t.setpos(-300,-300)
    t.pendown()
    t.circle(50)

def notenoughsides () :
    p = input('You cant have polygon with 2 or less sides')

main ()
