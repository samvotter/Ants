# libraries
from tkinter import *
import random as r
import time as t
import math as m


class Ant:

    def __init__(self, frame, WIDTH, HEIGHT, x, y, start):
        # beginning tile
        self.loc = start

        self.needToMake = True

        # canvas details
        self.frame = frame
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = y
        self.blockX = int(WIDTH/y)
        self.blockY = int(HEIGHT/x)
        self.destinationX = None
        self.destinationY = None
        self.posx = int(start.row)
        self.posy = int(start.col)

        self.memoryBuffer = ""

        # the previously visited tile
        self.last = None

        # amount contributed to the tile's value
        self.pheromone = {}
        self.pheromone[0] = 0
        self.pheromone[1] = 3

        # canvas details
        # state ([0:1,0:1] - [SEARCH : RETURN, WAITING : TRANSIT, DIRECTION: 0-North, 1-East, 2-South, 3-West]
        self.state = [0, 0, None]

    def move(self):

        # if where you want to go is where you are, pick somewhere new
        if self.destinationX == self.posx and self.destinationY == self.posy:
            self.state[1] = 0

        # if target is already going somewhere, ignore
        elif self.state[1]:
            if self.state[2] == 0:
                self.frame.move(self.image, 0, -1)
                self.posy -= 1
            elif self.state[2] == 1:
                self.frame.move(self.image, 1, 0)
                self.posx += 1
            elif self.state[2] == 2:
                self.frame.move(self.image, 0, 1)
                self.posy += 1
            elif self.state[2] == 3:
                self.frame.move(self.image, -1, 0)
                self.posx -= 1
            return

        # if they are standing on the start, they are searching
        if self.loc.start:
            self.state[0] = 0
            self.memoryBuffer = ""
            if self.last is not None:
                self.last = None

        # if they are standing on the target, reverse direction
        elif self.loc.target:
            self.loc.value += self.pheromone[1]*2
            self.state[0] = 1
            self.memoryBuffer = "".join(reversed(self.memoryBuffer))

        # if they are returning . . .
        if self.state[0]:
            if self.memoryBuffer[0] == "N":
                self.moveSouth()
            elif self.memoryBuffer[0] == "E":
                self.moveWest()
            elif self.memoryBuffer[0] == "S":
                self.moveNorth()
            elif self.memoryBuffer[0] == "W":
                self.moveEast()
            self.memoryBuffer = self.memoryBuffer[1:]
        else:
            # if they are are searching. . .
            N = self.lookUp(self.loc.connections["N"], "N")
            E = self.lookUp(self.loc.connections["E"], "E") + N
            S = self.lookUp(self.loc.connections["S"], "S") + E
            W = self.lookUp(self.loc.connections["W"], "W") + S
            choiceRange = W
            choice = r.uniform(0, choiceRange-1)
            if choice < N:
                self.memoryBuffer += "N"
                self.moveNorth()
            elif choice < E:
                self.memoryBuffer += "E"
                self.moveEast()
            elif choice < S:
                self.memoryBuffer += "S"
                self.moveSouth()
            elif choice < W:
                self.memoryBuffer += "W"
                self.moveWest()
            else:
                print("ERROR: INVALID SELECTION")

    def lookUp(self, NESW, entry):
        if NESW is not None:
            if entry == "N" and NESW.borders[2]:
                print("N is 0")
                return 0
            elif entry == "E" and NESW.borders[3]:
                print("E is 0")
                return 0
            elif entry == "S" and NESW.borders[0]:
                print("S is 0")
                return 0
            elif entry == "W" and NESW.borders[1]:
                print("W is 0")
                return 0
            if NESW == self.last:
                return 0
            else:
                return NESW.value
        else:
            return 0

    def moveNorth(self):
        self.last = self.loc
        self.loc = self.loc.connections["N"]
        self.state[1] = 1
        self.state[2] = 0
        self.destinationY = self.posy - self.blockY
        self.destinationX = self.posx
        self.loc.value += self.pheromone[self.state[0]]

    def moveEast(self):
        self.last = self.loc
        self.loc = self.loc.connections["E"]
        self.state[1] = 1
        self.state[2] = 1
        self.destinationX = self.posx + self.blockX
        self.destinationY = self.posy
        self.loc.value += self.pheromone[self.state[0]]

    def moveSouth(self):
        self.last = self.loc
        self.loc = self.loc.connections["S"]
        self.state[1] = 1
        self.state[2] = 2
        self.destinationY = self.posy + self.blockY
        self.destinationX = self.posx
        self.loc.value += self.pheromone[self.state[0]]

    def moveWest(self):
        self.last = self.loc
        self.loc = self.loc.connections["W"]
        self.state[1] = 1
        self.state[2] = 3
        self.destinationX = self.posx - self.blockX
        self.destinationY = self.posy
        self.loc.value += self.pheromone[self.state[0]]

    def turnAround(self):
        if self.state[2] == 0:
            self.memoryBuffer += "S"
            self.moveSouth()
        elif self.state[2] == 1:
            self.memoryBuffer += "W"
            self.moveWest()
        elif self.state[2] == 2:
            self.memoryBuffer += "N"
            self.moveNorth()
        elif self.state[2] == 3:
            self.memoryBuffer += "E"
            self.moveEast()
        else:
            print("ERROR: INVALID SELECTION")



    def createImage(self):
        if self.needToMake:
            self.image = self.frame.create_oval(self.loc.col * (self.width / self.y) + (self.width / self.y) / 3,
                                            self.loc.row * (self.height / self.x) + (self.height / self.x) / 3,
                                            (self.loc.col+1) * (self.width / self.y) - (self.width / self.y) / 3,
                                            (self.loc.row+1) * (self.height / self.x) - (self.height / self.x) / 3,
                                            fill="blue")
            self.posx = int(self.loc.row * (self.width / self.y) + (self.width / self.y) / 3)
            self.posy = int(self.loc.col * (self.height / self.x) + (self.height / self.x) / 3)
        self.needToMake = False



