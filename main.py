# Imports
import turtle as trtl
import random as rand

# Maze settings
numSides = 25
length = 20
color = "blue"
doorSize = length * 2
currentSide = 0
currentSize = length
beforeDoor = 0
beforeBarrier = 0

#Turtle settings
painter = trtl.Turtle()
painter.pencolor(color)
painter.speed("fastest")
painter.pensize(5)

def getRand():
    global beforeDoor
    global beforeBarrier
    beforeDoor = rand.randint(length * 2, (currentSize - length * 2))
    beforeBarrier = rand.randint(length * 2, (currentSize - length * 2))

def drawDoor(preDoor):
    global painter
    painter.forward(preDoor)
    painter.pencolor("magenta")
    painter.forward(doorSize)
    painter.pencolor(color)

def drawBarrier(preBarrier):
    painter.forward(preBarrier)
    painter.left(90)
    painter.forward(length * 2)
    painter.backward(length * 2)
    painter.right(90)

while(currentSide < numSides):
    if(currentSide >= 4):
        # Generate random numbers
        getRand()

        # Double check random numbers are valid - if not recalculate
        while abs(beforeDoor - beforeBarrier < length):
            getRand()

        # Door first
        if(beforeDoor < beforeBarrier):
            drawDoor(beforeDoor)
            drawBarrier(beforeBarrier - beforeDoor - length * 2)
            painter.forward(currentSize - beforeBarrier)

        # Barrier first
        else:
            drawBarrier(beforeBarrier)
            drawDoor(beforeDoor - beforeBarrier)
            painter.forward(currentSize - beforeDoor - length * 2)

        # Make sure to turn for the next wall
        painter.left(90)
    # Increase side number and size of wall
    currentSide += 1
    currentSize += length

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()


