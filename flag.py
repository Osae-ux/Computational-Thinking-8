import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-350, 100)

# stripe 1
t.color("dark green")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, 100)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-150, 100)

# stripe 3
t.color("dark red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.end_fill()

turtle.exitonclick()
