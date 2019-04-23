import Terrain as t

new = t.Terrain(5, 5)
new.addAnt()

for i in range(0, 10):
    new.textPrint()
    new.ants[0].move()

