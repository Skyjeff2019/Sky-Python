import turtle as t
t.bgcolor("blue")


t.speed(0)
for x in range(4):
    t.circle(100)
    t.right(3)
    t.pencolor("white")

for i in range(90):
    t.circle(100)
    t.right(4)

def circle2():
    t.pencolor("red")
    for l in range(45):
        t.circle(120)
        t.right(8)

circle2()
t.exitonclick()
