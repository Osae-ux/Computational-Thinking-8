# the code begins 
import turtle

t = turtle.Turtle()
# shapes with color
t.penup()
t.goto(100, 0)
t.color("red")
t.pendown()
for i in range(300):
    t.forward(152)
    t.left(122)
    t.speed(10)
t.penup()
t.goto(100, 100)
t.color("blue")
t.pendown()
for i in range(300):
    t.forward(152)
    t.left(122)
    t.speed(10)
t.penup()
t.goto(100, -200)
t.color("pink")
t.pendown()
for i in range(300):
    t.forward(152)
    t.left(122)
    t.speed(10)
t.penup()
t.goto(100, 100)
t.color("green")
t.pendown()
for i in range(300):
    t.forward(152)
    t.left(122)
    t.speed(10)
t.penup()
t.goto(0, 0)
t.color("orange")
t.pendown()
for i in range(300):
    t.forward(152)
    t.left(122)
    t.speed(10)

turtle.exitonclick()
#end of code