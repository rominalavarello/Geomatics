# ----------------- COVID CASES ------------------

from pyqgis_scripting_ext.core import *

# ----------------- FOLDERS ----------------------

folder = "/Users/rominalavarello/Downloads"
# folder = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics"
# folder = "C:/Users/Michele/OneDrive - Scientific Network South Tyrol/EMMA/Year 1/Advanced geomatics"
# folder = r"C:\Users\miria\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics"

gpkgPATH = folder + "/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"

data = "/Users/rominalavarello/Desktop/Geomatics/Covid_exercise"
# data = r"C:\Users\laura\OneDrive - Scientific Network South Tyrol\Documents\Master\Semester2\3.advanced geomatics\Group4"
# data = r"C:\Users\miria\OneDrive - Scientific Network South Tyrol\Semester 2\Advanced Geomatics\Group4"
# data = r""C:\Users\Michele\OneDrive - Scientific Network South Tyrol\EMMA\Year 1\Advanced geomatics\Group4""

covidPATH = data + "/dpc-covid19-ita-regioni.csv"

# output folder
outputFolder = "/Users/rominalavarello/Desktop/Geomatics/temp/outputCOVID/"

# -----------------------------------------------


# Load provinces layer: to read
provincesName = "ne_10m_admin_1_states_provinces"

# remove to update
HMap.remove_layers_by_name(["ne_10m_admin_1_states_provinces"])

provincesLayer = HVectorLayer.open(gpkgPATH, provincesName)
provincesFeatures = provincesLayer.features()

provincesLayer.subset_filter("iso_a2='IT'")


# Load to see layers
HMap.add_layer(provincesLayer)

# create dictionary with geometries
regionName2GeomMap = {}
regionIndex = provincesLayer.field_index("region")

for provinceFeature in provincesLayer.features():
    geometry = provinceFeature.geometry
    regionName = provinceFeature.attributes[regionIndex]
    
    regionGeometry = regionName2GeomMap.get(regionName) # or with IF
    # at first is empty so it will add 1 province, if it's not empty we need to union geometries
    if regionGeometry: #if it exists
        # pass
        regionGeometry = regionGeometry.union(geometry) #now is unioning if has already more than 1 geometries
    else: # if empty
        regionGeometry = geometry
    
    regionName2GeomMap[regionName] = regionGeometry # a set of all region names with 1 province

# for name, geom in regionName2GeomMap.items():
#     print(name, geom.asWkt()[:30])

# --------- DATA -------------

with open(covidPATH,'r') as file:
    lines = file.readlines()
    
day2featuresMap = {} # values (geom, cases, regionname) for each day
    
for index, line in enumerate(lines):
    line = line.strip()
    
    if index < 50000:
        # print(line)
        lineSplit = line.split(",")
        # 0 -> date
        # 3 -> region
        # 17 -> total cases
        # 4, 5 -> lat, lon
        
        dayAndTime = lineSplit[0]
        dayAndTime = dayAndTime.split("T")
        day = dayAndTime[0]
        
        if day.endswith("01"):
            region = lineSplit[3]
            totalCases = int(lineSplit[17])
            
            lat = float(lineSplit[4])
            lon = float(lineSplit[5])
            dataPoint = HPoint(lon, lat)
            
            for regionName, regionGeometry in regionName2GeomMap.items():
                if regionGeometry.intersects(dataPoint):
                    featureslist = day2featuresMap.get(day) # day will be our KEY
                    if featureslist:
                        featureslist.append((regionGeometry, [day, region, totalCases]))
                    else:
                        featureslist = [(regionGeometry, [day, region, totalCases])] #tupple
                    day2featuresMap[day] = featureslist

imagePathsList = []

for day, featureList in day2featuresMap.items():
    # if day != "2020-04-01":
    #     continue
        
    print("Generating day", day)
    newLayerName = "covid_italy"
    HMap.remove_layer_by_name(newLayerName)
    
    schema = {
        "day": "string",
        "region": "string",
        "totalCases": "int"
    }
    
    covidLayer = HVectorLayer.new(newLayerName, "MultiPolygon", "EPSG:4326", schema)
    
    for geometry, attributes in featureList:
        covidLayer.add_feature(geometry, attributes)
        
    # style = HFill('yellow') + HStroke('black',0.5)
    # covidLayer.set_style(style)
    
    # color table so by moving day by day it changes, but with same ranges: max and min for ALL dates
    ## for total cases
    ranges = [
        [float('-inf'),1000],
        [1001, 3000],
        [3001, 10000],
        [10001, 40000],
        [40001, 1000000],
        [1000001,float('inf')]
    ]
    
    styles = [
        HFill('mistyrose') + HStroke('white',0.5),
        HFill('lightcoral') + HStroke('white',0.5),
        HFill('indianred') + HStroke('white',0.5),
        HFill('firebrick') + HStroke('white',0.5),
        HFill('darkred') + HStroke('white',0.5),
        HFill('black') + HStroke('white',0.5)
    ]
    
    labelStyle = HLabel('totalCases', size = 8, color = 'black') + HHalo() + HFill()
    
    covidLayer.set_graduated_style("totalCases", ranges, styles, labelStyle)
    
    
    HMap.add_layer(covidLayer)
    
    printer = HPrinter(iface)
    mapProp = {
        "x": 5,
        "y": 25,
        "width": 285,
        "height": 180,
        "frame": True,
        "extent": covidLayer.bbox()
    }
    printer.add_map(**mapProp)
    
    #LEGEND
    
    legendProp = {
        "x": 210,
        "y": 30,
        "width": 150,
        "height": 100,
        "frame": True,
    }
    printer.add_legend(**legendProp)
    
    labelProp = {
        "x": 120,
        "y": 10,
        "text": "COVID Italy, total cases",
        "bold":True,
        "italic":False
    }
    printer.add_label(**labelProp)
    
    labelProp = {
        "x": 30,
        "y": 190,
        "text": day,
        "bold":True,
        "font_size": 28,
    }
    printer.add_label(**labelProp)

    
    imageName = f"{day}_covid.png"
    imagePath = f"{outputFolder}/{imageName}"
    printer.dump_to_image(imagePath)
    imagePathsList.append(imagePath)

# generate animation
# import pip 
# pip.main(['install','pillow'])

from PIL import Image

imagesList = []
for path in imagePathsList:
    img = Image.open(path)
    imagesList.append(img)
    
animationPath = f"{outputFolder}/covid_animation.gif"

imagesList[0].save(animationPath, save_all=True, append_images=imagesList[1:], duration=500, loop=2) #miliseconds, loop to restart

for path in imagePathsList:
    os.remove(path)








