# Imports
import turtle as trtl

#Setup Variables
numSides = 25
length = 20
color = "blue"
doorSize = 40
wallPiece = 5

#Turtle Settings
painter = trtl.Turtle()
painter.pencolor(color)
painter.speed("fastest")
painter.pensize(5)


currentSide = 0
currentSize = length
preBarrier = 40

while(currentSide < numSides):
    if(currentSide < 4):
        #painter.forward(currentSize)
        print("test")
    else:

        # Door Handle(r)
        painter.forward(wallPiece)
        painter.penup()
        painter.forward(doorSize)
        painter.pendown()

        # CFM Code Here
        painter.forward(preBarrier)
        painter.left(90)
        painter.forward(length*2)
        painter.right(180)
        painter.forward(length*2)
        painter.left(90)
        # Wall End

        painter.forward(currentSize - doorSize - wallPiece - preBarrier)

    painter.left(90)
    currentSize += length
    currentSide+=1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()