import pgzrun
import random

WIDTH = 505
HEIGHT = 605
TITLE = "Main game"

def draw():
    w = 150
    h = 250
    for i in range(20):
        squ = Rect(200, 200, w, h)
        squ.center = 200, 200
        # Generate random RGB values
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.draw.rect(squ, color)
        w += 10
        h -= 10 
    screen.draw.circle((50, 50), 30, "Blue")

pgzrun.go()
