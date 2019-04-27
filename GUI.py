# libraries
from tkinter import *
import time
import math as m

# modules
import Terrain as t


# helper function for button
def moreAnts():
    new.addAnt()
    for ant in new.ants:
        ant.createImage()

def go():
    timer = 0
    while True:
        timer += 1
        for ant in new.ants:
            ant.move()
        if timer == 1:
            new.decay()
        for row in new.land:
            for tile in row:
                tile.updateImage()
        main_window.update()
        time.sleep(SLEEPTIME)
        timer = timer % (DECAYRATE)

WIDTH = 1400
HEIGHT = 900
LANDX = 3
LANDY = 3
SLEEPTIME = .0001
DECAYRATE = int(m.sqrt((WIDTH/LANDY)**2+(HEIGHT/LANDX)**2)/3)


# LANDX = int(input("How many rows would you like?"))
# LANDY = int(input("How many columns would you like?"))

main_window = Tk()

frame = Canvas(main_window, width=WIDTH, height=HEIGHT)
new = t.Terrain(frame, WIDTH, HEIGHT, LANDX, LANDY)
Button(main_window, text="Add Ant", command=moreAnts).grid(row=0)
Button(main_window, text="Go", command=go).grid(row=0, column=1)
frame.grid(row=1, columnspan=2)

for row in new.land:
    for col in row:
        col.createImage()


main_window.mainloop()
