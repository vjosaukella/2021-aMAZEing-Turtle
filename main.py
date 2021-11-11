# Imports
import turtle as trtl

#Setup Variables
numSides = 25
length = 20
color = "blue"

#Turtle Settings
painter = trtl.Turtle()
painter.pencolor(color)
painter.speed("fastest")
painter.pensize(5)


currentSide = 0
currentSize = length
while(currentSide < numSides):
    painter.forward(currentSize)
    painter.left(90)
    currentSize += length
    currentSide+=1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()