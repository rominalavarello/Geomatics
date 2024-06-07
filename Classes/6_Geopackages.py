from pyqgis_scripting_ext.core import *


## ADD VIEW MAP

# HMap.remove_layers_by_name(["OpenStreetMap", "other map", citiesName, "test"])

folder = "/Users/rominalavarello/Desktop/Geomatics/"
gpkgPATH = folder + "miniGPKG.gpkg"

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

## READING AN EXISTING GPKG LAYER

countriesName = "ne_50m_admin_0_countries"
# to access the layer, we use the open method of the HVectorLayer class, passing the database path and the layer name: HVectorLayer
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)

print("Schema (first 4 fields):")

counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1 
    if counter < 5:
        print("\t", name, "of type", type)



## TO KNOW THE PROJECTION OF THE LAYER:

crs = countriesLayer.prjcode
print("Projection: ", crs)
print("Spatial extent: ", countriesLayer.bbox())
print("Feature count: ", countriesLayer.size()) # number of features (so multipolygon is 1 feature)



## using schema to query data

print("Attributes for Italy:")
# get features iterator: returning a list of all features:
countriesFeatures = countriesLayer.features()

# # get all field names:
# fieldNames = countriesLayer.field_names
# print(fieldNames)

# get the index of the field "NAME":
nameIndex = countriesLayer.field_index("NAME")
print(nameIndex)

for feature in countriesFeatures:
    # attributes are accesse via their index
    # if feature.attributes[nameIndex]=='Italy':        #SHORTER VERSION
    name = feature.attributes[nameIndex]
    if name == 'Italy':
        # print("Found it")
        geom = feature.geometry # get the geometry 
        print("GEOM:", geom.asWkt()[:100] + "...") 
#         count = 0
#         for index, attribute in enumerate(feature.attributes): 
#             print(fieldNames[index] + ":", attribute)
#             count += 1
#             if count > 5:
#                 print("...")
#                 break


# FILTER BY EXPRESSION

expression = "NAME like 'I%' and POP_EST > 3000000" 
filteredfeatures = countriesLayer.features(expression) 
count = 0
for feature in filteredfeatures:
    print(feature.attributes[nameIndex])
    count+=1
print("Feature count with filter: ", count)


lon = 11.119982
lat = 46.080428
point = HPoint(lon, lat)
buffer = point.buffer(2)

citiesName = "ne_10m_populated_places"
citiesLayer = HVectorLayer.open(gpkgPATH, citiesName)
HMap.add_layer(citiesLayer)

citiesNameIndex = citiesLayer.field_index("NAME")

# print("\napply bbox filter on features")

count = 0
for feature in citiesLayer.features():
    count += 1
print("Cities features listed:", count)

aoi = buffer.bbox()
count = 0
for feature in citiesLayer.features(bbox=aoi):    ## BOUNDING BOX
    print(feature.attributes[citiesNameIndex]) 
    count += 1
print("Count =", count)

count = 0
for feature in citiesLayer.features(geometryfilter=buffer):     ## GEOMETRY FILTER
    print(feature.attributes[citiesNameIndex])
    count += 1
print("Cities geatures listed with geometry filter: ",count)




###### CREATING DATA
### Memory vector layers: 

# Create a schema: is a dictionary, having as pairs the name and type of fields

fields = {
    "id": "Integer",
    "name": "String",
}

just2citiesLayer = HVectorLayer.new("test", "Point", "EPSG:4326", fields) # name of layer, type, coordsystem, fields

just2citiesLayer.add_feature(HPoint(-122.42, 37.78), [1, "San Francisco"])
just2citiesLayer.add_feature(HPoint(-73.98, 40.47), [2, "New York"])

# HMap.add_layer(just2citiesLayer)


# create geopackage file
path = folder + "test.gpkg" # GEOPACKAGE
error = just2citiesLayer.dump_to_gpkg(path, overwrite=True) # if you add a second layer you put overwrite=False
if(error):
    print(error)

# not as temporary file
testLayer = HVectorLayer.open(path, "test")
HMap.add_layer(testLayer)



## OTHER WITH MORE ATTRIBUTES

fields = {
    "name": "String",
    "population": "Integer",
    "lat": "Double",
    "lon": "Double"
}

oneCityMoreAttributes = HVectorLayer.new("test2", "Point", "EPSG:4326", fields)
oneCityMoreAttributes.add_feature(HPoint(-73.98, 40.47), \
                                    ["New York", 19040000, 40.47, -73.98])

error = oneCityMoreAttributes.dump_to_gpkg(path, overwrite=False) # for adding to the exxisting geopackage
if(error):
    print(error)
    