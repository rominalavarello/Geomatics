from math import cos, sin, radians
from pyqgis_scripting_ext.core import *


# CIRCLES
# For carthesian coords we need the angle in radians

# define an angle:
n = 7
d = 8
iterations = 20
maxAngle = 360*iterations
coords = []

for angle in range(0, maxAngle, 1):
    radAngle = radians(angle)
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)
    # print(x,y)
    
    coords.append([x,y])

lines = HLineString.fromCoords(coords)



canvas = HMapCanvas.new()
canvas.add_geometry(lines,"purple",2)

canvas.set_extent(lines.bbox())
canvas.show()