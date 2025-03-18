###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")

q1 = codesters.Square(100, 100, 200, 'green')
q2 = codesters.Square(-100, 100, 200, 'white')
q3 = codesters.Square(-100, -100, 200, 'pink')
q4 = codesters.Square(100, -100, 200, 'red')

s1 = codesters.Sprite("sea_salt2", 100, 100)
s1.set_size(0.7)
s2 = codesters.Sprite("drums", -100, 100)
s2.set_size(0.9)
s3 = codesters.Sprite("goat", -100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("sea", 100, -100)
s4.set_size(0.2)

message1 = codesters.Text("Oscar Cottrell Forman",0,220,"red")
message2 = codesters.Text("snake river farms",0,-220,"red")