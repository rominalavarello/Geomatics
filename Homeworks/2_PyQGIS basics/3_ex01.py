from pyqgis_scripting_ext.core import *

# 01
# Write a script that generates an UTM grid. Allow the user to change
# the zone extend.
# Input: the extent of the zone in degrees 
extent = 6
polygons = []

for lon in range(-180,180,extent):
    minX = lon
    maxX = lon + extent
    minY = -84
    maxY = 84
    
    coords = [[minX,minY],[minX,maxY],[maxX,maxY],[maxX,minY],[minX,minY]]
    polygon = HPolygon.fromCoords(coords)
    polygons.append(polygon)


canvas = HMapCanvas.new()

# osm = HMap.get_osm_layer()
# canvas.set_layers([osm])

for polygon in polygons:
    canvas.add_geometry(polygon)
    
canvas.set_extent([-180, -84, 180, 84])
canvas.show()

# different projections when you overlay, so we need to reproject