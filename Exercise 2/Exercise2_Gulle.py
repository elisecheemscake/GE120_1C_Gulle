"""
Exercise 2
Gulle, Jo Elise G.
2023-06414
"""
counter = 1
lines = []

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


    if "-" in azimuth:
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

    line = (counter, distance, bearing)
    lines.append(line)

    yesno = input("Add new line? ")
    if yesno.lower() == "Yes" or yesno.lower() == "y":
        counter = counter + 1
        continue
    else:
        break


print("\n\n")
print('{: ^10} {: ^10} {: ^10}'.format("LINE", "DISTANCE","BEARING"))

for line in lines:
    print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

print("\n\n")
print("----------END----------")