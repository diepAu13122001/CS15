from turtle import *

# pen
pensize(10)
color("aqua")
shape(name="circle")

# square
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

# circle
up()
setposition(0, -150)
down()
color("red")
circle(radius=20)

# 5 edges
up()
setposition(100, 0)
down()
color("pink")
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)

left(54 + 18)
backward(100)
right(108)
forward(100)
left(54 + 18)
forward(100)
left(54 + 18)
forward(100)
left(54 + 18)
forward(100)

# start
up()
setposition(100, 100)
down()
color("gray")

left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)
left(180-36)
forward(100)

mainloop()