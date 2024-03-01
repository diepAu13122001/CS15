from turtle import *

#  setup pen
shape("turtle")
pencolor("red")
fillcolor("green")
begin_fill()
# draw a square
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
end_fill()

# draw a diamond
penup()
setpos(-75, 50)
pendown()

right(45)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)


mainloop()