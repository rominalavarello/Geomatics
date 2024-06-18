from pyqgis_scripting_ext.core import *

folder = "/Users/rominalavarello/Desktop/Geomatics/"
gpkgPATH = folder + "miniGPKG.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_10m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"
tempfolder = "/Users/rominalavarello/Desktop/Geomatics/temp"

#cleanup
HMap.remove_layers_by_name(["OpenStreetMap", countriesName, citiesName, riversName, "rivers_italy"])

#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

# load layer: POINTS
citiesLayer = HVectorLayer.open(gpkgPATH, citiesName)

citiesLayer.subset_filter("SOV0NAME='Italy'")   ## filtering in a layer

## STYLING:
# for marker: shape, size, rotation 
# for fill: rgb code  OR "COLOR" + transparency
# for stroke: color + thickness
pointStyle = HMarker("square",3,45) + \
                HFill("1,83,94,200") + HStroke("lightblue",0.5)

#labels
field = "NAME"
# pointStyle += HLabel(field,yoffset=-6) + HHalo("white",1)

field = "if(POP_MAX>1000000, concat(NAME, ' (', round(POP_MAX/1000000,1), ')'), NAME)"


labelProperties = {
    "font": "Arial",
    "color": "darkgreen",
    "size": 12,
    "field": field,
    "xoffset": 0,
    "yoffset": -6
}    # dictionary

pointStyle += HLabel(**labelProperties) + HHalo("white",1)


citiesLayer.set_style(pointStyle)



# other layer: POLYGONS
countriesLayer = HVectorLayer.open(gpkgPATH, countriesName)
countriesLayer.subset_filter("NAME='Italy'")
italyGEOM = countriesLayer.features()[0].geometry    #extract the 1st because i know is just 1 feature now

polygonStyle = HFill("190,207,80,150") + HStroke("darkgreen",1)
countriesLayer.set_style(polygonStyle)



# other layer: LINES
riversLayer = HVectorLayer.open(gpkgPATH, riversName)
riversLayerItaly = riversLayer.sub_layer(italyGEOM,"rivers_italy",['scalerank','name'])    # it creates a new layer: geom, namenewlayer, fieldstomaintain

## thematic styling: list of lists
ranges = [
    [0,0], #the biggest
    [1,5],
    [6,7],
    [8,9],
    [10,11]
]

styles = [
    HStroke("darkblue",5),
    HStroke("steelblue",4),
    HStroke("skyblue",3),
    HStroke("paleturquoise",2),
    HStroke("lightcyan",1)
]

labelStyle = HLabel (**labelProperties) + HHalo("white",1)

riversLayerItaly.set_graduated_style('scalerank', ranges, styles, labelStyle)




# lineStyle = HStroke("lightcyan",1)

# labelProperties = {
#     "font": "Arial",
#     "color": "darkblue",
#     "size": 14,
#     "field": 'name',
#     "along_line": True,      #to follow direction of the line
#     "bold": True,
#     "italic": True
# }


# lineStyle += labelStyle
# riversLayerItaly.set_style(lineStyle + labelStyle)



HMap.add_layer(countriesLayer)
HMap.add_layer(riversLayerItaly)
HMap.add_layer(citiesLayer)






# LAYOUT: A4
### cambio el sistema de coordenadas a EPSG:4326, porque mis layers estan en ese y qgis tenia otro


printer = HPrinter(iface)
mapProperties = {
    "x": 5,
    "y": 25,
    "width": 285,
    "height": 180,
    "extent": [10,44,12,46],   # or bounding box: countriesLayer.bbox(),
    "frame":True
}

labelProperties = {
    "x": 120,
    "y": 10,
    "text": "Such a nice map",
    "font_size": 28,
    "bold": True,
    "italic": False
    
}

legendProperties = {
    "x": 215, # mm
    "y": 30,
    "width": 150,
    "height": 100,
    "max_symbol_size": 3 # not mm
}

scalebarProperties = {
    "x": 10,
    "y": 190,
    "units": "km",
    "segments": 4,
    "unit_per_segment": 10,
    "style": "Single Box",
    "font_size": 12
}


printer.add_map(**mapProperties)
printer.add_label(**labelProperties)
printer.add_legend(**legendProperties)
printer.add_scalebar(**scalebarProperties)


outputPdf = f"{tempfolder}/test.pdf"
printer.dump_to_pdf(outputPdf)

outputpng = f"{tempfolder}/test.png"
printer.dump_to_image(outputpng)

