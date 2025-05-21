# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - adding the Variables
x1 = -250
y1 = 250
x2 = -250
y2 = 175
x3 = -250
y3 = 100
x4 = -250
y4 = 25
# Section 3 - Setup
set_background("castle")
t1 = create_sprite("tik",x1,y1)
t2 = create_sprite("fred",x2,y2)
t3 = create_sprite("food",x3,y3) 
t4 = create_sprite("chuck",x4,y4)


# Racing part
# x2 is fastest because the lowest speed is still faster than x3's fastest speed
time.sleep(3)
for i in range(30):
	x1 += 20
	x2 += random.randint(100,120)
	x3 += 90
	x4 += 5
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	


# Section 5 - Winner
if x1 >= x2 and x1 >= x3 and x1 >= x4:
 	print("tik wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("fred wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
	print("food wins!")
elif x4 >= x1 and x4 > x2 and x4 >= x1:
	print("chuck wins!")



turtle.exitonclick()
