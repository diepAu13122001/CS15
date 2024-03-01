from turtle import *

# setup pen
pensize(15)
pencolor("pink")
shape("turtle")

# big square
penup()
setposition(0, 50)
pendown()

right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)

# small square
color("green")
pensize(7)
penup()
setposition(-25, 25)
pendown()

right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)


mainloop()
