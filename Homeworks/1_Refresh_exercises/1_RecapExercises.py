folder = "/Users/rominalavarello/Desktop/Geomatics"

## Excercise 1

age=25
name = "Mario Rossi"
activity = "skating"
job = "engineer"

print(f"Hey, I am {name}.\n I am {age} and I love to go {activity} \n I work as an {job}")
print("--------------")

## Excercise 2

ex2path = f"{folder}/data/01_exe2_data.csv"

with open(ex2path, 'r') as file:
    lines = file.readlines()
    
for line in lines:
    print(line)
    
for line in lines:
    line = line.strip()
    lineSplit = line.split(";")
    #print(lineSplit)
    
    analogString = lineSplit[0]
    analogSplit = analogString.split(":")
    x1 = float(analogSplit[1])
    #print(x1)
    
    maxvoltageString = lineSplit[1]
    y2 = float(maxvoltageString[11:])
    #print(x1,y2)
    
    maxanalogString = lineSplit[2]
    x2 = float(maxanalogString.split(":")[1])
    #print(x1,y2,x2)
    
    # x2/x1 = y2/y1
    y1 = y2 * x1/x2
    
    print(x1, x2, y1, y2)

print("--------------")

## Excercise 3

string = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s"
new_string = string.replace(',', ';')
print(new_string)

print("--------------")

## Excercise 4

lista = list(range(1, 6))
print(lista)

for i in lista:
    print(i)
    
print("--------------")

## Excercise 5

for i in lista:
    print(f"Number {i}")

print("--------------")

## Excercise 6

lista2=[10,20,30,40,50,60,70,80,90,100]

for i in lista2:
    if i < 55:
        print(f"Number {i}")
        
print("--------------")

## Excercise 7

list1=[1,2,3,4,5]
list2 = ["first", "second", "third", "fourth", "fifth"]

for i in range(len(list1)):
    print(f"{list2[i]} is {list1[i]}")

print("--------------")
  
## Excercise 8
string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

characters_count = 0
characters_no_espaces = 0
words_count = 0

characters_count += len(string)
characters_no_espaces += len(string.replace(" ", ""))
words_count += len(string.split())

print(f"Characters count: {characters_count}")
print(f"Characters count without spaces: {characters_no_espaces}")
print(f"Words count: {words_count}")
print("--------------")

## Excercise 9

ex9path = f"{folder}/data/01_exe9_data.csv"
with open(ex9path, 'r') as file:
    lines9 = file.readlines()

for line in lines9:
    print(line)

print("----")

for line in lines9:
    line = line.strip()
    if not line.strip().startswith('#') and len(line) != 0:
        print(line)
        
print("--------------")
    
## Excercise 10

for line in lines9:
    line = line.strip()
    if not line.strip().startswith('#') and len(line) != 0:
        # print(line) 
        linedivision = line.split(",")
        value = float(linedivision[1])
        if value < 1000 and value > 0:
            print(line)
print("--------------")

## Excercise 11

ex11path = f"{folder}/data/01_exe11_data.csv"
with open(ex11path, 'r') as file:
    lines11 = file.readlines()
    
for line in lines11:
    line = line.strip()
    print(line)

for line in lines11:
    line = line.strip()
    ## item.split: separa key de value por "=", dejando: key=value
    data = dict(item.split('=') for item in line.split(';'))
    base = float(data['base'].replace('cm', ''))
    height = float(data['height'].replace('cm', ''))
    area = (base * height) / 2
    print(f"base * height / 2 = {base} * {height} = {area} cm2")

## OTRA FORMA: 
### nota: no funciona pq en base hay un numero de ms digitos, comparado con los otros.

# BaseMap = {}
# HeightMap = {}

# for line in lines11:
#     line = line.strip()
#     linesplit11 = line.split(";")
    
#     base = linesplit11[0]
#     basevalue = float(base[-4:-2])
    
#     height = linesplit11[1]
#     heightvalue = float(height[7:])
    
#     BASEvalues = BaseMap.get(base,[])
#     BASEvalues.append(basevalue)
#     BaseMap[base] = BASEvalues
    
#     HEIGHTvalues = HeightMap.get(height,[])
#     HEIGHTvalues.append(heightvalue)
#     HeightMap[height] = HEIGHTvalues
    
#     area = basevalue * heightvalue / 2
    
#     print(f"base * height / 2 = {basevalue} * {heightvalue} = {area} cm2")

print("--------------")


## Excercise 12

who = {
    "Daisy": 11,
    "Joe": 201,
    "Will": 23,
    "Hanna": 44
}

what={
    44: "runs",
    11: "dreams",
    201: "plays",
    23: "walks"
}

where = {
    44: "to town.",
    11: "in her bed.",
    201: "in the livingroom.",
    23: "up the mountain."
}

for name, cod in who.items():
    action = what.get(cod)
    location = where.get(cod)
    print(f"{name} {action} {location}")

print("--------------")

## Excercise 13

list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["c", "d", "e", "f", "g", "h", "a"]
list3 = ["c", "d", "e", "f", "g"]
list4 = ["c", "d", "e", "h", "a"]

Lists = list1 + list2 + list3 + list4

counting_letters = {}

for letter in Lists:
    counting_letters[letter] = counting_letters.get(letter, 0) + 1
    
for letter, count in sorted(counting_letters.items()):
    print(f"count of {letter} = {count}")

print("--------------")

## Excercise 14

STATIONSpath = f"{folder}/data/stations.txt"

with open(STATIONSpath, 'r') as file:
    lines14 = file.readlines()
    
for line in lines14[:20]:
    line = line.strip()
    print(line)

print("--------------")

## Excercise 15

with open(STATIONSpath, 'r') as file:
    lines15 = file.readlines()
    
linesCount = 0

for line in lines15:
    line = line.strip()
    if len(line) != 0:
        linesCount += 1

print(linesCount)

print("--------------")

## Excercise 16

with open(STATIONSpath, 'r') as file:
    lines16 = file.readlines()

for line in lines16:
    line = line.strip()
    lineSplit = line.split(",")
    
print(f"Number of columns: {len(lineSplit)}")
print("--------------")

## Excercise 17

with open(STATIONSpath, 'r') as file:
    lines17 = file.readlines()

for line in lines17[:20]:
    line = line.strip()
    lineSplit = line.split(",")
    # print(lineSplit)
    stationID = lineSplit[0]
    stationNAME = lineSplit[1].strip()
    print(f"{stationID}, {stationNAME}")

print("--------------")

## Excercise 18

with open(STATIONSpath, 'r') as file:
    lines18 = file.readlines()

sum_cum = 0
count = 0

for line in lines18[1:]:
    line = line.strip()
    lineSplit = line.split(",")
    Height = float(lineSplit[5])
    sum_cum += Height
    count += 1
print(sum_cum)
print(count)
print(f"Average height: {sum_cum/count} cm")

print("--------------")

## Excercise 19

with open(STATIONSpath, 'r') as file:
    lines19 = file.readlines()

count = 0
sum_cum = 0
available_fields = []

for line in lines19[1:]:
    line = line.strip()
    lineSplit = line.split(",")
    Height = float(lineSplit[5])
    sum_cum += Height
    count += 1
averageValue = sum_cum / count

line_titles = lines19[0].strip()
fields = line_titles.split(",")
available_fields.extend(fields)
#print(available_fields)
    
import os
file_name = os.path.basename(STATIONSpath)

### Summary
print(f"File info: {file_name}")
print("-------")
print(f"Stations count: {count}")
print(f"Average value: {averageValue}")
print("Available fields:")
for field in available_fields:
    print(f" -> {field.strip()}")
print()
print("First data lines:")
for line in lines19[:5]:
    line = line.strip()
    print(line)

print("--------------")

## Excercise 20
ex20path = f"{folder}/data/station_data.txt"

with open(ex20path,'r') as file:
    lines20 = file.readlines()

count20 = 0
sum_cum20 = 0
available_fields20 = []

for line in lines20[1:]:
    line = line.strip()
    lineSplit = line.split(",")
    RR = float(lineSplit[3])
    if RR >= 0:
        sum_cum20 += RR
        count20 += 1
averageValue20 = sum_cum20 / count20

line_titles20 = lines20[0].strip()
fields20 = line_titles20.split(",")
available_fields20.extend(fields20)

file_name20 = os.path.basename(ex20path)

### Summary
print(f"File info: {file_name20}")
print("-------")
print(f"Stations count: {count20}")
print(f"Average value: {averageValue20}")
print("Available fields:")
for field in available_fields20:
    print(f" -> {field.strip()}")
print()
print("First data lines:")
for line in lines20[:5]:
    line = line.strip()
    print(line)

print("--------------")

# Excercise 21
n=10
m=5

for i in range(n):
    line = "*" * m
    print(line)

print("--------------")

# Excercise 22
n = 10
for i in range(1, n+1):
    line = "*" * i
    print(line)

print("--------------")

# Excercise 23
n = 10
for i in range(n, 0, -1):
    line = "*" * i
    print(line)
    
print("--------------")

# Excercise 24
a = 10
suma_ac = 0

for i in range(1,a+1):
    if i % 2 == 0:
        suma_ac += i
        # print(i)
print(suma_ac)

print("--------------")

# Excercise 25
numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]

suma_acc = 0

for i in numbers:
    if i % 2 == 0:
        suma_acc += i
print(suma_acc)

print("--------------")

# Excercise 26
ex26path1 = f"{folder}/data/01_exe26_dataset1.csv"
ex26path2 = f"{folder}/data/01_exe26_dataset2.csv"

dataset1_dict = {}

with open(ex26path1, "r") as file:
    lines = file.readlines()
    headers = lines[0].strip().split(',')
    for line in lines[1:]:
        fields = line.strip().split(',')
        id = fields[0]
        data = fields[1:]
        dataset1_dict[id] = data

print("ID,Value1,Value2,Value3,Value4")

with open(ex26path2, "r") as file:
    lines = file.readlines()
    for line in lines[1:]:
        fields = line.strip().split(',')
        id = fields[0]
        if id in dataset1_dict:
            dataset1_data = dataset1_dict[id]
            print(f"{id},{','.join(dataset1_data)},{','.join(fields[1:])}")

print("--------------")







