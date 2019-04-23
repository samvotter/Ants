import random as r

class Ant:

    def __init__(self, start):
        # beginning tile
        self.loc = start

        # the previously visited tile
        self.last = None

        # amount contributed to the tile's value
        self.pheromone = 1

        # canvas details
        # state ([0:1,0:1] - [SEARCH : RETURN, WAITING : TRANSIT]
        self.state = [0, 0]

    def move(self):
        # if target is already going somewhere, ignore
        if self.state[1]:
            pass
        # if they are standing on the start, they are searching
        elif self.loc.start:
            self.state[0] = 0
        # if they are standing on the target, reverse direction
        elif self.loc.target:
            self.state[0] = 1
            self.state[1] = 1
            self.loc = self.last
            return
        # if they are are searching. . .
        N = self.lookUp(self.loc.connections["N"])
        E = self.lookUp(self.loc.connections["E"]) + N
        S = self.lookUp(self.loc.connections["S"]) + E
        W = self.lookUp(self.loc.connections["W"]) + S
        choiceRange = W
        choice = r.randint(0, choiceRange-1)
        print(choice)
        print(N)
        print(E)
        print(S)
        print(W)
        if choice < N:
            self.last = self.loc
            self.loc = self.loc.connections["N"]
            self.state[1] = 1
            self.loc.value += self.pheromone
        elif choice < E:
            self.last = self.loc
            self.loc = self.loc.connections["E"]
            self.state[1] = 1
            self.loc.value += self.pheromone
        elif choice < S:
            self.last = self.loc
            self.loc = self.loc.connections["S"]
            self.state[1] = 1
            self.loc.value += self.pheromone
        elif choice < W:
            self.last = self.loc
            self.loc = self.loc.connections["W"]
            self.state[1] = 1
            self.loc.value += self.pheromone
        else:
            print("ERROR: INVALID SELECTION")

    def lookUp(self, NESW):
        if NESW is not None:
            if NESW == self.last:
                return 0
            else:
                return NESW.value
        else:
            return 0


