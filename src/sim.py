#imports
from vpython import *
from consts import *

scene.title = "Simple Pendulum Simulation"
scene.width = 500
scene.height = 500
scene.background = color.gray(0)

pivot = vector(0, 1.2, 0)
pendulumPivot = box(pos=pivot, size=vector(1, 1, 1), color=color.white)

def setPendulumCoords(angle, length):
    global pivot
    deltaX = length * sin(angle)
    deltaY = length * cos(angle)
    x = pivot.x + deltaX
    y = pivot.y - deltaY
    return vector(x, y, 0)

pendulum = sphere(pos=setPendulumCoords(ANGLE, LENGTH), radius=0.5, color=color.red)
rod = cylinder(pos=pivot, axis=(pendulum.pos-pivot), radius=0.1, color=color.gray(0.9))

while True:
    rate(100)