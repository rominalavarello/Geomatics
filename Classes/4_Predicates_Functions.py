# PREDICATES AND FUNCTIONS

from pyqgis_scripting_ext.core import *

# FIGURES
g1 = HPolygon.fromCoords([[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]])
g2 = HPolygon.fromCoords([[5, 0], [5, 2], [7, 2], [7, 0], [5, 0]])
g3 = HPoint(4, 1)
g4 = HPoint(5, 4)
g5 = HLineString.fromCoords([[1, 0], [1, 6]])
g6 = HPolygon.fromCoords([[3, 3], [3, 6], [6, 6], [6, 3], [3, 3]])

# 
print("polygon boungingboz:", g1.bbox())
print("polygon length:", g1.length())
print("polygon area:", g1.area())

print("line length:", g5.length())
print("line area:", g5.area())

print("point length:", g3.length())
print("point area:", g3.area())

# distance between geometries, nearest points
print("distance between geometries:", g5.distance(g4))



# PREDICATES: functions that return true or false

## INTERSECTS: do they touch g1?
print("intersects")
print(g1.intersects(g2))
print(g1.intersects(g3))
print(g1.intersects(g4))
print(g1.intersects(g5))
print(g1.intersects(g6))

## TOUCHES: at least 1 point in common, but not intersect the interior?
print("touches")
print(g1.touches(g2))
print(g1.touches(g3))
print(g1.touches(g4))
print(g1.touches(g5))
print(g1.touches(g6))

## CONTAINS
print("contains")
print(g1.contains(g2))
print(g1.contains(g3))
print(g1.contains(g4))
print(g1.contains(g5))
print(g1.contains(g6))


# FUNCTIONS
## INTERSECTIONS
## / 2 polygons: area, / polygon and line: line, / polygon and point: point, / 2 lines: line or point.
print("intersection")
print(g1.intersection(g6))
print(g1.intersection(g2))
print(g1.intersection(g3))
print(g1.intersection(g5))

newGeom = g1.intersection(g6)

## SYMDIFFERENCE: opposit, portions not shared
print("symdifference")
print(g1.symdifference(g6))
print(g1.symdifference(g2))
print(g1.symdifference(g3))
print(g1.symdifference(g5))

newGeom = g1.symdifference(g6)

### result of symdifference of 2 polygons: MULTIPOLYGON
### result of symdifference of 2 touching polygons: single polygon
### result of symdifference of polygon containing a point: same polygon
### so, not always we have an homogenous return.

## UNION: both merged in 1 feature. 
## ONLY SAME GEOMETRIES
print("union")
print(g1.union(g6))
print(g1.union(g2))
print(g1.union(g3))
print(g1.union(g5))

newGeom = g1.union(g6)
newGeom1 = g1.union(g2)

## DIFFERENCE: 
## ORDER MATTERS
print("difference")
print(g6.difference(g1))

print(g1.difference(g5)) # additional coord where line intersects
print(g1.difference(g5)) # will get same polygon

newGeom1 = g6.difference(g1)

## BUFFERS: geenerate polygon around
### buffer point: 
### 2nd value, points per quadrants. so like sides of polygon.
### by default, 8 points.
b1 = g3.buffer(1.0)
b2 = g3.buffer(1.0,2)

### buffer lines
b3 = g5.buffer(1)
b4 = g5.buffer(1,2)

### flat ending: for flexes or vertices
### -1 IS DONT USE IT OR USE DEFAULT.
# b5 = g5.buffer(1, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_ROUND)
b5 = g5.buffer(0.5, -1, JOINSTYLE_ROUND, ENDCAPSTYLE_SQUARE)


## CONVEX HULL
##create a border containing set of geometries
collection = HGeometryCollection([g1,g2,g3,g4,g5,g6])
hull = collection.convex_hull()



canvas = HMapCanvas.new()

canvas.add_geometry(g1, "red", 2)
canvas.add_geometry(g2, "pink", 2)
canvas.add_geometry(g3, "yellow", 2)
canvas.add_geometry(g5, "purple", 2)
canvas.add_geometry(g6, "orange", 2)
canvas.add_geometry(g4, "cyan", 2)

# canvas.add_geometry(newGeom,'magenta',3)
# canvas.add_geometry(newGeom1,'cyan',3)
# canvas.add_geometry(b1, "pink", 2)
# canvas.add_geometry(b2, "orange", 2)
# canvas.add_geometry(b3, "red", 2)
# canvas.add_geometry(b4, "purple", 2)
# canvas.add_geometry(b5, "yellow", 2)
canvas.add_geometry(hull, "black", 2)


# canvas.set_extent([-1, -1, 10, 10])
canvas.set_extent(hull.bbox())
canvas.show()
