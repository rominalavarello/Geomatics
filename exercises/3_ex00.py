from pyqgis_scripting_ext.core import *

folder = "/Users/rominalavarello/Desktop/Geomatics"

# 00
# Write a script that reads geometries from 02_exe0_geometries.csv 
# and draws them on a new map canvas.

filePath = f"{folder}/data/02_exe0_geometries.csv"

with open(filePath,'r') as file:
    lines = file.readlines()

forms = []

for line in lines:
    fline  = line.strip()
    lineSplit = line.split(";")
    formline = lineSplit[0]
    coordsline = lineSplit[1]
    
    # put all coords into a list of [pairs] divided by "," 
    # so [[x,y],[x,y]...]
    # AND make each value into numbers
    coordsList = []
    for coordline in coordsline.split():
        x, y = map(float, coordline.split(","))
        coordsList.append([x, y])
    
    if formline == "point":
        for x,y in coordsList:
            form = HPoint(x,y)
    if formline == "line":
        form = HLineString.fromCoords(coordsList)
    if formline == "polygon":
        form = HPolygon.fromCoords(coordsList)
    
    forms.append(form)

colors = ["red","purple","orange","pink","yellow"]

canvas = HMapCanvas.new()
for i in range(len(forms)):
    color = colors[i]
    form = forms[i]
    canvas.add_geometry(form,color,2)
canvas.set_extent([0, 0, 40, 40])
canvas.show()

