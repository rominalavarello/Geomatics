# 01 - CONVERT THE STATIONS FILE TO GEOPACKAGE

from pyqgis_scripting_ext.core import *

def convert_coords(coords):
    list = []
    for latorlon in coords:
        grados = float(latorlon[0])
        minutos = float(latorlon[1])
        segundos = float(latorlon[2])
        
        sign = 1 if grados >= 0 else -1
        
        decimales = abs(grados) + minutos / 60 + segundos / 3600
        decimales *= sign
        
        list.append(decimales)
    
    return list

folder = "/Users/rominalavarello/Documents/EMMA/2 semester/Advanced geomatics/excercises1/"
path = folder + "stations.txt"

with open(path, 'r') as file:
    lines = file.readlines()

# for line in lines[:5]:
#     line = line.strip()
#     lineSplit = line.split(",")
#     print(lineSplit)

fields = {
    "id":"int",
    "station":"str",
    "country":"str",
    "lat":"str",
    "lon":"str",
    "elevation":"int"
    }

stationslayer = HVectorLayer.new("stations", "Point", "EPSG: 4326", fields)
HMap.remove_layers_by_name(["stations","stations_forever"])

latitudes = []
longitudes = []

for line in lines[:500]:
    if not line.startswith("#"):
        line = line.strip()
        lineSplit = line.split(",")
        # print(lineSplit)
        
        lat = lineSplit[3]
        # print(lat)
        latSplit = lat.split(":")
        latitudes.append(latSplit)
        
        lon = lineSplit[4]
        lonSplit = lon.split(":")
        longitudes.append(lonSplit)
        
        name = lineSplit[1]
        
        LATs = convert_coords(latitudes)
        LONs = convert_coords(longitudes)
        
        for lat,lon in zip(LATs,LONs):
            stationslayer.add_feature(HPoint(lon,lat),[1,name])
    
# print(LATs)

# AS TEMPORARY FILE
HMap.add_layer(stationslayer)


# GEOPACKAGE

gpkgpath = folder + "test.gpkg" # GEOPACKAGE
error = stationslayer.dump_to_gpkg(path, overwrite=True)
if(error):
    print(error)

# not as temporary file
stationslayerF = HVectorLayer.open(gpkgpath, "stations_forever")
HMap.add_layer(stationslayerF)