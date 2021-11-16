# Imports
import turtle as trtl
import random as rand

#Setup Variables
numSides = 6
length = 20
color = "blue"
doorSize = length * 2
beforeDoor = 5

#Turtle Settings
painter = trtl.Turtle()
painter.pencolor(color)
#painter.speed("fastest")
painter.pensize(5)


currentSide = 0
currentSize = length
preBarrier = 40

while(currentSide < numSides):
    if(currentSide < 4):
        #painter.forward(currentSize)
        print("")
    else:
        #beforeDoor = rand.randint(length*2, currentSize - length*2)
        #preBarrier = rand.randint(length*2, currentSize - length*2)
        beforeDoor = 10
        preBarrier = 20

        if(beforeDoor < preBarrier):

            # Door Handle(r)
            painter.forward(beforeDoor)
            #painter.penup()
            painter.pencolor("magenta")
            painter.forward(doorSize)
            painter.pencolor(color)
            #painter.pendown()

            # CFM Code Here
            painter.forward(preBarrier - beforeDoor - length * 2)
            painter.left(90)
            painter.forward(length*2)
            painter.right(180)
            painter.forward(length*2)
            painter.left(90)
            # Wall End

            painter.forward(currentSize - doorSize - beforeDoor - preBarrier)

        else:
            # CFM Code Here
            painter.forward(preBarrier)
            painter.left(90)
            painter.forward(length * 2)
            painter.right(180)
            painter.forward(length * 2)
            painter.left(90)
            # Wall End

            # Door Handle(r)
            painter.forward(beforeDoor - preBarrier - length * 2)
            # painter.penup()
            painter.pencolor("magenta")
            painter.forward(doorSize)
            painter.pencolor(color)
            # painter.pendown()

            painter.forward(currentSize - doorSize - beforeDoor - preBarrier)
    painter.forward(currentSize)
    painter.left(90)
    currentSize += length
    currentSide+=1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()