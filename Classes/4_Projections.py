from pyqgis_scripting_ext.core import *

# PROJECTIONS
## helper class: use a starting and a destination projection
crsHelper = HCrs()
crsHelper.from_srid(4326) #spetial reference system ID
crsHelper.to_srid(32632) 

point4326 = HPoint(11,46)
newpointin32632 = crsHelper.transform(point4326)

print(f"{point4326} -> {newpointin32632}")

## inverse transform
backTo4326 = crsHelper.transform(newpointin32632, inverse=True)
print(backTo4326)


## for stations file: OSM 3857
### take geom of utm from 4326 to 3857

# extent = 6
# polygons = []

# for lon in range(-180,180,extent):
#     minX = lon
#     maxX = lon + extent
#     minY = -84
#     maxY = 84
    
#     coords = [[minX,minY],[minX,maxY],[maxX,maxY],[maxX,minY],[minX,minY]]
#     polygon = HPolygon.fromCoords(coords)
#     polygons.append(polygon)


# canvas = HMapCanvas.new()

# osm = HMap.get_osm_layer()
# canvas.set_layers([osm])

# for polygon in polygons:
#     canvas.add_geometry(polygon)
    
# canvas.set_extent([-180, -84, 180, 84])
# canvas.show()
