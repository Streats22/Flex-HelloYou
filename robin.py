Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> turtle.setup(400, 400, 0, 0)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    turtle.setup(400, 400, 0, 0)
NameError: name 'turtle' is not defined
>>> import turtle
>>> turtle.setup(400, 400, 0, 0)
>>> turtle.forward(100)
>>> turtle.forward(100)
>>> turtle.reset()
>>> turtle.color("blue")
>>> turtle.forward(100)
>>> trutle.right(45)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    trutle.right(45)
NameError: name 'trutle' is not defined
>>> 
right(45)
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    right(45)
NameError: name 'right' is not defined
>>> turtle.right(45)
>>> turtle.fowrard(100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    turtle.fowrard(100)
AttributeError: module 'turtle' has no attribute 'fowrard'
>>> turtle.forward(100)
>>> turtle.right(45)
>>> turtle.forward(100)
>>> turtle.right(45)
>>> turtle.forward(100)
>>> turtle.color("#A2FF33")
>>> venster = turtle.getscreen()
>>> venster.bgcolor("yellow")
>>> turtle.reset()
>>> turtle.bgcolor("#FFFFF")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    turtle.bgcolor("#FFFFF")
  File "<string>", line 8, in bgcolor
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1237, in bgcolor
    color = self._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1158, in _colorstr
    raise TurtleGraphicsError("bad color string: %s" % str(color))
turtle.TurtleGraphicsError: bad color string: #FFFFF
>>> turtle.pencolor("#FFFFFF")
>>> turtle.fillcolor("#FF0000")
>>> turtle.begin_fill()
>>> turtle.forward(100)
>>> turtle.bgcolor("black")
>>> turtle.right(120)
>>> turtle.forward(100)
>>> turtle.right(120)
>>> turtle.forward(100)
>>> 