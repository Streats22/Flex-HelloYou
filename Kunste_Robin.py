import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
turtle.speed(14)
my_pen = turtle.Pen()
turtle.bgcolor("black")
x = 5
for x in range(650):
   my_pen.pencolor(colors[x % 5])
   my_pen.width(x/45 + 5)
   my_pen.forward(100)
   my_pen.left(65)
   my_pen.forward(120)
   my_pen.left(35)

turtle.done()
