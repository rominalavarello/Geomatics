# Geometries, multigeometries, colors

from pyqgis_scripting_ext.core import *

# point
point = HPoint(30.0, 10.0)
print(point.asWkt())

# line string, list of little lists with xx and y
coords = [[31,11], [10,30], [20,40], [40,40]]
line = HLineString.fromCoords(coords)
print(line.asWkt())

# polygon, clos on the first coordinate
## This will be the exterior ring of the polygon.
coords = [[32,12], [10,20], [20,39], [40,39], [32,12]]
polygon = HPolygon.fromCoords(coords)
print(polygon)

## If the polygon contains holes, they can be passed as rings, i.e. closed linestrings:
exteriorPoints = [[35,10],[10,20],[15,40],[45,45],[35,10]]
holePoints = [[20,30],[35,35],[30,20],[20,30]]
### Create the polygon using the exterior ring. 
polygonWithHole = HPolygon.fromCoords(exteriorPoints)
### Create the hole ring. --> linear ring = polygon because it closes.
holeRing = HLineString.fromCoords(holePoints)
### Add the hole ring to the polygon.
polygonWithHole.add_interior_ring(holeRing)
print(polygonWithHole.asWkt())

# Multigeometry: list of lists of coordinates. we don't usually create them by hand'
## multipoint
coords = [[10,40],[40,30],[20,20],[30,10]]
multiPoints = HMultiPoint.fromCoords(coords)
print(multiPoints)
##  multiline
coords1 = [[10,10],[20,20],[10,40]]
coords2 = [[40,40],[30,30],[40,20],[30,10]]
multiLine = HMultiLineString.fromCoords([coords1, coords2])
print(multiLine)
## multipolygon
coords1 = [[30,20], [10,40], [45,40], [30,20]]
coords2 = [[15,5], [40,10], [10,20], [5,10], [15,5]]
multiPolygon = HMultiPolygon.fromCoords([coords1, coords2])
print(multiPolygon)
## multipolygon with a ring: made from polygons, not from coords.
# polygon1 = HPolygon.fromCoords(coords1)
# polygon1.add_interior_ring(...)
# polygon2 = HPolygon.fromCoords(coords2)
# multiPolygon = HMultiPolygon([polygon1, polygon2])


# Access just 1 geometry, or extract it
## to return selected geometries
subGeometries = multiPolygon.geometries()
colors_list = ["purple","cyan","green"]
## access to coordinantes
coordinates = polygon.coordinates()
for coord in coordinates:
    print(f"coord x = {coord[0]} / coord y = {coord[1]}")

# inverse asWkt: to have string to geometries
wkt = "POINT (156 404)"
pointGeom = HGeometry.fromWkt(wkt)
print(pointGeom)

wkt = """MULTIPOLYGON (((130 510, 140 450, 200 480, 210 570, 150 630, 130 560, 130 510)),
  ((430 770, 370 820, 210 860, 20 760, 35 631, 100 370, 108 363, 154 284, 230 380,
      140 400, 150 440, 130 450, 104 585, 410 670, 440 590, 450 590, 430 770)))
"""
polygonGeom = HGeometry.fromWkt(wkt)
print(polygonGeom)


# visualization: create a canvas
canvas = HMapCanvas.new()

canvas.add_geometry(point, "red", 2)
canvas.add_geometry(multiPoints,"red",2)
# canvas.add_geometry(line, "blue", 2)
canvas.add_geometry(multiLine,"blue",2)
# canvas.add_geometry(polygon, "green", 2)
canvas.add_geometry(multiPolygon,"green",1)
canvas.add_geometry(polygonWithHole, "magenta", 10)

for i in range(len(subGeometries)):
    color = colors_list[i]
    polugon = subGeometries[i]
    canvas.add_geometry(polugon,color,2)

# couldn't do it
# for i in polygonGeom:
#     polugon = polygonGeom[i]
#     canvas.add_geometry(polugon,"red",2)

## locate where to look: Min x, min y, max xx, max y.
canvas.set_extent([0, 0, 50, 50])
canvas.show()