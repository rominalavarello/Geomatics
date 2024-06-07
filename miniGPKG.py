# CREATE A GEOPACKAGE WITH USEFUL LAYERS:

from pyqgis_scripting_ext.core import *

folder = "/Users/rominalavarello/Desktop/Geomatics/"
gpkgPATH = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"

# Path for the new GeoPackage
gpkgpath = folder + "miniGPKG.gpkg"

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# Layer names in the source GeoPackage
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_10m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"

# Open the layers from the source GeoPackage
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)
citiesLayer = HVectorLayer.open(gpkgPATH, citiesName)
riversLayer = HVectorLayer.open(gpkgPATH, riversName)

# HMap.add_layer(countriesLayer)

#Dump layers into the new GeoPackage
error = countriesLayer.dump_to_gpkg(gpkgpath, overwrite=True)
if error:
    print(f"Error dumping countries layer: {error}")

error = citiesLayer.dump_to_gpkg(gpkgpath, overwrite=False)
if error:
    print(f"Error dumping cities layer: {error}")

error = riversLayer.dump_to_gpkg(gpkgpath, overwrite=False)
if error:
    print(f"Error dumping rivers layer: {error}")

# Open layers from the new GeoPackage
countriesLayerF = HVectorLayer.open(gpkgpath, "Countries")
HMap.add_layer(countriesLayerF)

citiesLayerF = HVectorLayer.open(gpkgpath, "Cities")
HMap.add_layer(citiesLayerF)

riversLayerF = HVectorLayer.open(gpkgpath, "Rivers")
HMap.add_layer(riversLayerF)
