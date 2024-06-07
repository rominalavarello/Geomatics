from pyqgis_scripting_ext.core import *

folder = "/Users/rominalavarello/Desktop/Geomatics"
csvPath = f"{folder}/data/stations.txt"

with open(csvPath, 'r') as file:
    lines = file.readlines()
    # print(lines)
    
stations = []
stationsxcn = {}
Names = []

for line in lines[1:]:
    line = line.strip()
    lineSplit = line.split(",")
    # print(lineSplit)
    
    ID = lineSplit[0]
    name = lineSplit[1].strip()
    cn = lineSplit[2]
    lat = lineSplit[3].replace("+","")
    lon = lineSplit[4].replace("+","")
    height = lineSplit[5]
    
    lonSplit = lon.split(":")
    LON = float(lonSplit[0])+float(lonSplit[1])/60+float(lonSplit[2])/3600
    
    latSplit = lat.split(":")
    LAT = float(latSplit[0])+float(latSplit[1])/60+float(latSplit[2])/3600
    
    point = HPoint(LON,LAT)
    stations.append(point)
    
    ################################
    
    stationsxcn[cn] = stationsxcn.get(cn, 0) + 1
    
    Names.append(name)
    
for country, count in stationsxcn.items():
        print(f"{country}: {count}")
    

# TRANSFORMATION
## for stations file: OSM 3857
### take geom of utm from 4326 to 3857: EPSG:4326 (WGS84) to EPSG:3857 (Web Mercator) 

crsHelper = HCrs()
crsHelper.from_srid(4326) #spatial reference system ID
crsHelper.to_srid(3857) 

Stations = []

for point in stations:
    Point = crsHelper.transform(point)
    Stations.append(Point)

print(Stations[3])
print(stations[3])


collection = HGeometryCollection(Stations)
hull = collection.convex_hull()



########################################

## EXCERCISE 03

Lon = 11.34999
Lat = 46.49809

check_point = HPoint(Lon, Lat)
checkPoint = crsHelper.transform(check_point)

# considering that the lists keep the order we can use the lists of Name, Stations 
# and distances(that is created directly in the dictionary:

stationsDist_Names = {}
stationsDist_Stat = {}
for Name,Station in zip(Names,Stations):
    distance = checkPoint.distance(Station)
    stationsDist_Names[distance] = Name
    stationsDist_Stat[distance] = Station
    
min_distance = min(stationsDist_Names.keys())
nearest_station_name = stationsDist_Names[min_distance]
nearest_station_coords = stationsDist_Stat[min_distance]

print(f"Nearest station to the point {checkPoint}: {nearest_station_name}, coords: {nearest_station_coords}, distance: {min_distance}")



########################################

## EXCERCISE 04

# checkPoint = antes
radiusKM = 20000
# Stations

buffer = checkPoint.buffer(radiusKM)
stationsIN = []

for Station in Stations:
    if buffer.intersects(Station) == True:
        stationsIN.append(Station)

# for stationIN in stationsIN:
#     print({stationIN})

stations_Names = {}
stations_Dist = {}

for Name,Station in zip(Names,Stations):
    distance = checkPoint.distance(Station)
    Distance = distance/1000
    stations_Names[Station] = Name
    stations_Dist[Name] = Distance

for stationIN in stationsIN:
    name = stations_Names[stationIN]
    distance = stations_Dist[name]
    print(f"{name} ({distance:.2f} km): {stationIN}") 


#################


canvas = HMapCanvas.new()
canvas.add_geometry(buffer,"magenta",2)
for point in Stations:
    canvas.add_geometry(point, "cyan",2)
osm = HMap.get_osm_layer()
canvas.set_layers([osm])
# canvas.set_extent(hull.bbox())
canvas.set_extent(buffer.bbox())
canvas.show()






