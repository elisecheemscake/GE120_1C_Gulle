"""
Exercise 3
Gulle, Jo Elise G.
2023-06414
"""
#getting needed math functions from math module
from math import cos, sin, radians, sqrt

#defining new, needed funtions
def getLatitude(distance, azimuth):
    '''
    Solves for the latitude of a given line.
    Input: distance, azimuth
    Return: latitude
    '''
    latitude = -distance*cos(radians(float(azimuth)))
    return latitude

def getDeparture(distance, azimuth):
    '''
    Solves for the departure of a given line.
    Input: distance, azimuth
    Return: latitude
    '''
    departure = -distance*sin(radians(float(azimuth)))
    return departure

def azimuthToBearing(azimuth):
    '''
    Converts azimuths into bearings.
    Input: azimuth (in DD)
    Return: bearing (in DD)
    '''
    if "-" in str(azimuth):
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = ((int(degrees))+(int(minutes)/60)+(float(seconds)/3600))
    else:
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^5} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^5} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth <270:
        bearing = 'N {: ^5} E'.format(azimuth - 180)
    elif azimuth >270 and azimuth <360:
        bearing = 'S {: ^5} E'.format(360 - azimuth)
    elif azimuth == 0:
        bearing = "Due South"
    elif azimuth == 90:
        bearing = "Due West"
    elif azimuth == 180:
        bearing = "Due North"
    elif azimuth == 270:
        bearing = "Due East"
    else:
        bearing = "???"

    return bearing

#initializing counter, list of tuples, summations of lat, dep, and distance
counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

print("---------- TRAVERSE COMPUTATION ----------")

while True:
    print()
    print("Line No.", counter)

    #stops the user from inputting anything other than numbers
    try:
        distance = float(input("Distance: "))
    except ValueError:
        print("\n Invalid input. Please input numbers only.\n")
        continue

    #asks for azimuth
    azimuth = input("Azimuth (S): ")

    #converting azimuth to bearing using newly defined function
    bearing = azimuthToBearing(azimuth)

    #getting lat and dep using newly defined function
    lat = getLatitude(azimuth=float(azimuth),distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth),distance=float(distance))

    #summation variables increase with each loop
    sumLat = sumLat + lat
    sumDep = sumDep + dep
    sumDist = sumDist + float(distance)

    #putting all necessary information in a tuple, and putting that tuple back into the initial list
    line = (counter, distance, bearing, lat, dep)
    lines.append(line)

    #asks if the user wishes to continue adding more lines, breaks the loop if no
    yesno = input("Add new line? (Y/N) ")
    if yesno.lower() == "Yes" or yesno.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

#printing out the table of lines
print()
print('{: ^10} {: ^10} {: ^10} {: ^15} {: ^30}'.format("LINE", "DISTANCE","BEARING","LATITUDE","DEPARTURE"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], line[3], line[4]))

#printing out the summations
print()
print("SUMMATION OF LATITUDE: ", sumLat)
print("SUMMATION OF DEPARTURE: ", sumDep)
print("SUMMATION OF DISTANCE: ", sumDist)
print()

#getting the lec
lec = sqrt((sumLat**2) + (sumDep**2))
print("LEC: ", lec)

#getting the rec
rec = sumDist//lec
print("REC: 1:", rec)
print()

#start of traverse adjustment
print('{: ^30} {: ^30}'.format('LATITUDE CORRECTION', 'DEPARTURE CORRECTION'))

#getting only distances from the each tuple in the big list of tuples
distance_list = [element[1] for element in lines]

#initializing summation of dep and lat corrections
sum_corrDep = 0
sum_corrLat = 0

#getting the lat and dep corrections for each distance in the distance list
#also adds up the corrections at the end
for dist in distance_list:
    corrDep = -sumDep*(dist/sumDist)
    corrLat = -sumLat*(dist/sumDist)
    print('{: ^30} {: ^30}'.format(corrLat, corrDep))
    sum_corrDep = sum_corrDep + corrDep
    sum_corrLat = sum_corrLat + corrLat

print()
print('{: ^60}'.format('SUMMATION'))
print('{: ^30} {: ^30}'.format(sum_corrLat, sum_corrDep))

#initializing summation of adjusted lat and dep
sum_adjLat = 0
sum_adjDep = 0

print()
print('ADJUSTED LATITUDE')
#getting only latitudes from the each tuple in the big list of tuples
latitude_list = [element[3] for element in lines]

#adjusting lat
for latitude in latitude_list:
    adj_lat = latitude + corrLat
    print(adj_lat)
    sum_adjLat = sum_adjLat + adj_lat
print('SUMMATION:', sum_adjLat)

print()
print('ADJUSTED DEPARTURE')
#getting only departures from the each tuple in the big list of tuples
departure_list = [element[4] for element in lines]

#adjusting dep
for departure in departure_list:
    adj_dep = departure + corrDep
    print(adj_dep)
    sum_adjDep = sum_adjDep + adj_dep
print('SUMMATION:', sum_adjDep)

print()
print("---------- END ----------")