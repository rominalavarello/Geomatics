# exercise 03: CREATE A GPKG WITH THE COUNTRIES CENTROIDS

from pyqgis_scripting_ext.core import *

folder = "/Users/rominalavarello/Desktop/Geomatics/"
gpkgPATH = folder + "miniGPKG.gpkg"

HMap.remove_layers_by_name(["centroids",countriesName,"OpenStreetMap"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesName = "ne_50m_admin_0_countries"

schema = {
    "name":"string",
}

centroidsLayer = HVectorLayer.new("centroids","Point","EPSG: 4326", schema)
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)

nonInCountryList = []
nameIndex = countriesLayer.field_index("NAME")
for country in countriesLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    
    centroidsLayer.add_feature(centroid, [name])
    
    if not centroid.intersects(countryGeom):
        nonInCountryList.append(name)
    
simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo ()
centroidsLayer.set_style(simpleStyle)
HMap.add_layer(centroidsLayer)    # temporary layer

print("Countries with centroids outside:")
for c in nonInCountryList:
    print(c)
    


#############

ranges = [
    [80000000, float('inf')],
    [1000000, 80000000],
    [float('-inf'),1000000]
]

styles = [
    HFill("255, 0, 0, 70"),
    HFill("0, 255, 0, 70"),
    HFill("0, 0, 255, 70"),
]
    
labelstyle = HLabel("POP_EST") + HHalo()

countriesLayer.set_graduated_style("POP_EST", ranges, styles, labelstyle)

HMap.add_layer(countriesLayer)