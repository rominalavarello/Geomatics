from pyqgis_scripting_ext.core import *
## ADD VIEW MAP

osm = HMap.get_osm_layer()
# HMap.add_layer(osm)

folder = "/Users/rominalavarello/Desktop/Geomatics/"
gpkgPATH = folder + "miniGPKG.gpkg"


# COUNTRIES

countriesName = "ne_50m_admin_0_countries"
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)

print("Schema (first 20 fields):")
counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1 
    if counter < 21:
        print("\t", name, "of type", type)

countriesFeatures = countriesLayer.features()

# get all field names:
fieldNames = countriesLayer.field_names
print(fieldNames)

# crs = countriesLayer.prjcode
# print("Projection: ", crs)
# print("Spatial extent: ", countriesLayer.bbox())
# print("Feature count: ", countriesLayer.size())

    # Projection:  EPSG:4326
    # Spatial extent:  [-180.0, -89.99892578125, 180.0, 83.599609375]
    # Feature count:  242


# get the index of the field "NAME":
nameIndex = countriesLayer.field_index("NAME")
print(nameIndex)

for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == 'France':
        frechGeom = feature.geometry # get the geometry 
        print("GEOM:", frechGeom.asWkt()[:100] + "...") 


# CITIES

citiesName = "ne_10m_populated_places"
citiesLayer = HVectorLayer.open(gpkgPATH, citiesName)
# HMap.add_layer(citiesLayer)


fieldNames = citiesLayer.field_names
print(fieldNames)

citiesFeatures = citiesLayer.features()

cityIndex = citiesLayer.field_index("NAME")
print(cityIndex)

countcities = 0

for feature in citiesFeatures:
    name = feature.attributes[cityIndex]
    citiespoints = feature.geometry
    # print("GEOM:", citiespoints.asWkt()[:100] + "...") 
    # print(name)



# INTERSECTION

    if citiespoints.intersects(frechGeom):
        countcities += 1
        print(name,": ",citiespoints)

print(countcities)



