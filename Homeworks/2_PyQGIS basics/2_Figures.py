from pyqgis_scripting_ext.core import *

# FIGURE
g1 = HPolygon.fromCoords([[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]])
g2 = HPolygon.fromCoords([[5, 0], [5, 2], [7, 2], [7, 0], [5, 0]])
g3 = HPoint(4, 1)
g4 = HPoint(5, 4)
g5 = HLineString.fromCoords([[1, 0], [1, 6]])
g6 = HPolygon.fromCoords([[3, 3], [3, 6], [6, 6], [6, 3], [3, 3]])

collection = HGeometryCollection([g1,g2,g3,g4,g5,g6])
hull = collection.convex_hull()

canvas = HMapCanvas.new()
canvas.add_geometry(g1, "black", 2)
canvas.add_geometry(g2, "purple", 2)
canvas.add_geometry(g3, "blue", 2)
canvas.add_geometry(g4, "red", 2)
canvas.add_geometry(g5, "green", 2)
canvas.add_geometry(g6, "yellow", 2)
canvas.set_extent(hull.bbox())
canvas.show()



