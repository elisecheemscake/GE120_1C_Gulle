class Parcel():
    def __init__(self, owner, area):
        self.owner = str(owner)
        self.area = int(area)
    # defining the parameters of the parcel class

    def getClassification(self):
        '''
        Tells you how the parcel is classified according to its area.
        Input: Area
        Return: Classification
        '''
        if self.area < 10000:
            print("Residential")
        elif self.area > 10000 and self.area < 120000:
            print("Private Agricultural")
        elif self.area > 120000:
            print("Public Agricultural")
    # gets the classification of the parcel according to how large its area is
        
    def __str__(self):
        print("A parcel of land owned by " + str(self.owner) + " with an area of " + str(self.area) + " square meters.")
    # overloads the 'print' function - now it returns a whole sentence including the owner of the parcel and its area.

    def __add__(self, other):
        return "Consolidated lot of " + self.owner + " and " + other.owner + " with a total area of " + str(self.area + other.area) + " square meters."
    # overloads the + operator - now it adds the areas of two parcels and gives a description.

class Riparian(Parcel):
    def __init__(self, owner, area, type):
        self.owner = str(owner)
        self.area = int(area)
        self.type = int(type)
    # defining parameters of the Riparian subclass

    def getAdjoiningWaterbody(self):
        '''
        Tells you how the Riparian parcel is classified according to its type.
        Input: Type
        Return: Classification
        '''
        if self.type == 1:
            print("Adjacent to River - can be subject to titling")
        elif self.type == 2:
            print("Adjacent to Ocean (Littoral) - cannot be subject to titling")
        else:
            print("Invalid Riparian Parcel")
    # tells you the classification of the parcel according to its type - also prints a more detailed description
