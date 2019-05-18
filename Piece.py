class Piece(object):

    def __init__(self, image, name, location):
        if isinstance(image and name, str) and isinstance(location, tuple):
            self.image = image
            self.name = name
            self.location = location
        else:
            raise TypeError("One or more arguments dont macth type.\n X & Y must be int, image and name must be str and location must be a tuple")

    def getImage(self):
        return self.image

    def setImage(self, img):
        if isinstance(img, str):
            self.image = img
        else:
            raise TypeError("value must be a string")

    def getName(self):
        return self.name

    def setName(self, newName):
        if isinstance(newName, str):
            self.name = newName
        else:
            raise TypeError("value must be a string")

    def getLocation(self):
        return self.location

    def setLocation(self, newLocation):
        if isinstance(newLocation, tuple):
            self.location = newLocation
        else:
            raise TypeError("Location must be a tuple")

