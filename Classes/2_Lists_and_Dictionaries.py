# LISTS: sequence of objects, usually strings and numbers, also some geographic things

mylist = ['merano', 'Bolzano', 'Trento']
print(mylist)
print("The elements start at position 0: ", mylist[0])

## add objets and remove objects
mylist.append("Postdam")
print(mylist)

mylist.remove("Postdam")
print(mylist)

### remove by position: pop also returns the removed item
mylist.pop(0)
print(mylist)

## to check if my list includes something
mylist = ['merano', 'Bolzano', 'Trento']
doIHaveBolzano = "Bolzano" in mylist
print(doIHaveBolzano)

doIHavePostdam = "Postdam" in mylist
print(doIHavePostdam)


# Looping for lists
## excecutes it for each item
for item in mylist:
    print(item)

## if data comes from different sources but we want to put every item with position

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

### ranges create a series of numbers as an index
### excluding the last number
### list have to be of equal length

for index in range(len(colors)):
    color = colors[index]
    ratio = ratios[index]
    
    print(f"{colors} -> {ratio}")

# ***
# colors2 = colors.copy()
# colors2.sort()
# print(colors)
# print(colors2)
# ***

## break a loop
### it doesn't exxecute whatever comes after the break
for i in range(10):
    if i == 5:
        break
    print(f"A) {i}")

print("__________")

## continue allows you to skip the condition and keeps going with the rest of the code for loop
for i in range(10):
    if i == 5:
        continue
    print(f"B) {i}")

print("__________")


# other arguments of range
for i in range(2, 10):
    print(f"C) {i}")
## cada 2
### only for integer numbers, not floating points (decimales)
for i in range(0, 10, 2):
    print(f"D) {i}")

for i in range(10, 0, -2):
    print(f"E) {i}")

print("__________")


# Sorting lists
## sorts internally the list, sort it soes not retun anything
### so print(mylist.sort()) will not return anything
mylist = ['merano', 'Bolzano', 'Trento']
print(f"My original list: {mylist}")
mylist.sort()
print(f"My sorted list: {mylist}")

## other way, creo que es volver a lo anterior
mylist.sort(reverse = True)
print(f"My re-sorted list: {mylist}")

## the sorting follows the uppercase and lowercase
mylist = ["banana", "Orange", "Kiwi", "cherry"]
mylist.sort()
print(f"A mixed case list, sorted: {mylist}")
### to solve this:
mylist.sort(key = str.lower)
print(f"A mixed case list, properly sorted: {mylist}")


##  alphabetical sort
numlist =["002", "01", "3", "004"]
numlist.sort()
print(numlist)

## to have a numerical sort, we need to convert into numbers
numlist =["002", "01", "3", "004"]

def toInt(string):
    return int(string)
### int or float or whatever

numlist.sort(key = toInt)
print(numlist)

#### key = ... is only to compare process inside the mechanism of sort


# joining lists
abc = ["a", "b", "c"]
cde = ["c", "d", "e"]

newabcde = abc + cde
print(newabcde)

## to create a comma separated values, converting into a list
print(";".join(newabcde))
print("|".join(newabcde))     #pipe

numlist = [1.0,2.0,3.5,6,11,34,12]
print(max(numlist))
print(min(numlist))
print(sum(numlist))

print("__________")

# calculate average of a list usinf for loop

suma = 0

for i in range(len(numlist)):
    suma += numlist[i]
    print(suma)

print("__________")

suma = 0
count = 0

for i in range(len(numlist)):
    suma += numlist[i]
    count+=1
    print(suma)

average = suma/count
print(average)

average2 = suma/i
print(average)


print("__________")

diferencia = 0
diferencias = []
squaredvalues =[]
sumaSquared = 0

for n in range(len(numlist)):
    diferencia += numlist[n] - average
    diferencias.append(diferencia)
    squaredvalues.append(diferencia**2)
    sumaSquared += squaredvalues[n]
    
print(diferencias)
print(squaredvalues)
print(sumaSquared)

variance = sumaSquared/n-1
print(variance)


# ****************


# DICTIONARIES _ in{}

## key (is unique, and case sensitive): value

townsProvincesMap = {
    "merano": "BZ",
    "bolzano": "BZ",
    "trento": "TN"
}
print(townsProvincesMap)

## access values inside a dictionary
print(townsProvincesMap["merano"])

## add a new value
townsProvincesMap["postdam"] = "BR"
print(townsProvincesMap)

## remove: pop takes the key, 
### beacuse dictionaries does not have a position
townsProvincesMap.pop("postdam")
print(townsProvincesMap)

## ask if its in dictionary and get it
print(townsProvincesMap.get("Merano"))

if townsProvincesMap.get("Merano") is None:
    print("key doesn't exist")
else: 
    print("key exists")

### get also as a second argument to give a default value

print(townsProvincesMap.get("Merano", "unknown"))


## dictionaries have pairs
### items to collect the pairs.

for key, value in townsProvincesMap.items():
    print(key, "is in the province of", value)

## access keys, to sort a dictionary

print(townsProvincesMap.keys())
print(townsProvincesMap.values())

### sort by its key, first convert an iterable sequence into a list

keys = list(townsProvincesMap.keys())
keys.sort()
print(keys)

### print key and value, bcs now it is a list
#### give me the value of that particular key
for key in keys:
    print(key, "is in the province of", townsProvincesMap[key])


# ************


# READING AND WRITING TEXTFILES

## a file that does not exists
filePath = "/Users/rominalavarello/Documents/EMMA/2 semester/Advanced geomatics/excercises1/data_class2.txt"

data_class2 = """# stationid, datetime, temperature
1, 2022-01-01 00:00, 12.3

2, 2022-01-01 00:00, 11.3
3, 2022-01-01 00:00, 10.3
"""
#### w: open in writing mode, overwrites

with open(filePath, 'w') as file:
    file.write(data_class2)
    
#### a: append
with open(filePath, 'a') as file:
    file.write("1, 2023-01-02 00:00, 9.3")
    file.write("\n2, 2023-01-02 00:00, 8.3")

#### r: reading
##### readlines will be a list of lines
with open(filePath, 'r') as file:
    lines = file.readlines()
    
print(lines)

print("-----------")
## count stations using dictionaries
## creating a dictionary, we use the station id as key and asign values

stationsCount = {}

for line in lines:
    line = line.strip()
    if line.startswith("#") or len(line) == 0:
        continue
    linesplit = line.split(",")
    stationid = linesplit[0]
    
    ##### if that key does not exists, return 0 (as value)
    counter = stationsCount.get(stationid,0)
    counter += 1
    
    stationsCount[stationid] = counter
    
    print(stationsCount)
print("-----------")
print(stationsCount)