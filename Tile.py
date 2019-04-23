import random as r
import math as m


class Tile:

    def __init__(self, **kwargs):
        # The attractiveness of going to this tile
        self.value = 5

        # Connections
        self.connections = {}
        self.connections["N"] = None
        self.connections["E"] = None
        self.connections["S"] = None
        self.connections["W"] = None

        # features
            # Borders (0:1, if 1 then border is impassible)
            # Traits (0:1)
        self.borderN = False
        self.borderE = False
        self.borderS = False
        self.borderW = False

        self.start = False
        self.target = False

        # canvas details