import random as r
import math as m


class Tile:

    def __init__(self, frame, WIDTH, HEIGHT, x, y, i, j):
        # canvas details
        self.frame = frame
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = y

        # The attractiveness of going to this tile
        self.minimum = 5
        self.value = self.minimum

        # grid position
        self.row = i
        self.col = j

        # Connections
        self.connections = {}
        self.connections["N"] = None
        self.connections["E"] = None
        self.connections["S"] = None
        self.connections["W"] = None

        # features
            # Borders ([N, E, S, W] if 1 then border is impassible)
            # Traits (0:1)
        self.borders = [0, 0, 0, 0]

        self.start = False
        self.target = False

        # canvas details

    def modBorder(self, index):
        if self.borders[index]:
            self.borders[index] = 0
        else:
            self.borders[index] = 1

    def _from_rgb(self, rgb):
        return "#%02x%02x%02x" % rgb

    def createImage(self):
        self.image = self.frame.create_rectangle(self.col * (self.width / self.y),
                                                 self.row * (self.height / self.x),
                                                 (self.col + 1) * (self.width / self.y),
                                                 (self.row + 1) * (self.height / self.x), fill=self._from_rgb((0,0,0)))
        if self.start:
            self.frame.create_oval(self.col * (self.width / self.y),
                                   self.row * (self.height / self.x),
                                   (self.col + 1) * (self.width / self.y),
                                   (self.row + 1) * (self.height / self.x), fill=self._from_rgb((0,255,0)))

        if self.target:
            self.frame.create_oval(self.col * (self.width / self.y),
                                   self.row * (self.height / self.x),
                                   (self.col + 1) * (self.width / self.y),
                                   (self.row + 1) * (self.height / self.x), fill=self._from_rgb((255,0,0)))

    def updateImage(self):
        c = self.value
        if c > 255:
            c = 255
        self.frame.itemconfig(self.image, fill=self._from_rgb((c,c,c)))

