import Tile as t
import Ant as a

import random as r
import math as m


class Terrain:

    def __init__(self, x, y):
        self.land = []
        for i in range(0, x):
            self.land.append([])
            for j in range(0, y):
                self.land[i].append(t.Tile())
        for i in range(0, x):
            for j in range(0, y):
                if i - 1 >= 0:
                    self.land[i][j].connections["N"] = self.land[i - 1][j]
                if j + 1 < y:
                    self.land[i][j].connections["E"] = self.land[i][j + 1]
                if i + 1 < x:
                    self.land[i][j].connections["S"] = self.land[i + 1][j]
                if j - 1 >= 0:
                    self.land[i][j].connections["W"] = self.land[i][j - 1]
        self.startx = 0
        self.starty = 0
        self.targetx = 0
        self.targety = 0
        while m.sqrt((self.startx - self.targetx) ** 2 + (self.starty - self.targety) ** 2) < m.sqrt(
                x ** 2 + y ** 2) / 3:
            self.startx = r.randint(0, x - 1)
            self.starty = r.randint(0, y - 1)
            self.targetx = r.randint(0, x - 1)
            self.targety = r.randint(0, y - 1)
        self.land[self.startx][self.starty].start = True
        self.land[self.targetx][self.targety].target = True

        self.ants = []

    def addAnt(self):
        self.ants.append(a.Ant(self.land[self.startx][self.starty]))

    def textPrint(self):
        for row in range(0, len(self.land)):
            for col in range(0, len(self.land[row])):
                if self.land[row][col].start:
                    print("[S]", end=" ")
                elif self.land[row][col].target:
                    print("[T]", end=" ")
                else:
                    if self.ants[0].loc == self.land[row][col]:
                        print("[A]", end=" ")
                    else:
                        print("[ ]", end=" ")
            print("")
        print("")

        # canvas details