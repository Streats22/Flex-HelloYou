import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
YEEET = turtle.Turtle()

YEEET.speed(10)

for x in range(180):
    YEEET.pencolor(colors[x % 6])
    YEEET.forward(100)
    YEEET.right(30)
    YEEET.forward(20)
    YEEET.left(60)
    YEEET.forward(50)
    YEEET.right(30)

    YEEET.penup()
    YEEET.setposition(0, 0)
    YEEET.pendown()

    YEEET.right(2)

turtle.done()
