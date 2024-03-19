"""
Exercise 3
Gulle, Jo Elise G.
2023-06414
"""

from math import cos, sin, radians, sqrt

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


counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

print("----------LINE TABULATION----------")

while True:
    print()
    print("Line No.", counter)

    #stops the user from inputting anything other than numbers
    try:
        distance = float(input("Distance: "))
    except ValueError:
        print("\n Invalid input. Please input numbers only.\n")
        continue


    azimuth = input("Azimuth (S): ")

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth),distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth),distance=float(distance))

    sumLat = sumLat + lat
    sumDep = sumDep + dep
    sumDist = sumDist + float(distance)

    line = (counter, distance, bearing, lat, dep)
    lines.append(line)

    yesno = input("Add new line? (Y/N)")
    if yesno.lower() == "Yes" or yesno.lower() == "y":
        counter = counter + 1
        continue
    else:
        break


print("\n\n")
print('{: ^10} {: ^10} {: ^10} {: ^15} {: ^30}'.format("LINE", "DISTANCE","BEARING","LATITUDE","DEPARTURE"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2], line[3], line[4]))

print("\n")
print("SUMMATION OF LATITUDE: ", sumLat)
print("SUMMATION OF DEPARTURE: ", sumDep)
print("SUMMATION OF DISTANCE: ", sumDist)
print("\n")

lec = sqrt((sumLat**2) + (sumDep**2))
print("LEC: ", lec)

rec = sumDist//lec
print("REC: 1:", rec)

print("\n\n")
print("----------END----------")