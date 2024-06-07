# Excercise
# monthly sum of rain 

## read data into lines list

folder = "/Users/rominalavarello/Desktop/Geomatics/data/"
dataPath = folder + "01_exe_rain_data_1year.txt"

with open(dataPath, 'r') as file:
    lines = file.readlines()

## print 5 first lines
print(lines[:6])

monthMap = {}

## parse each line to extract the date (str) and value (num)
for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    #print(f"{date}, {value}")
    linesplit = line.split(",")
    date = linesplit[0]
    value = float(linesplit[1])
    #print (date,": ",value)
    
    ## aggregate the values by month, i.e. collect all values
    ### creating a dictionary that has month as a key.

    ### 1. extract the year-motnh from date

    month = date[:-2]
    #print(month, ": ", value)
    
    #### values will be at first an empty list
    #### estas agregando valores a la lista de values para cada mes (unico)
    values = monthMap.get(month, [])
    values.append(value)
    monthMap[month] = values
    
for month, values in monthMap.items():
    print(month,values)

for month, values in monthMap.items():
    cum_pp = sum(values)
    print(f"Cumulated rain for month {month} is {cum_pp}")

    
    
    
    
    