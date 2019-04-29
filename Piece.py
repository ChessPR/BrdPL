class Piece(object):

    def __init__(self, x, y, image, name, location):
        if isinstance(x and y, str) and isinstance(image and name, str) and isinstance(location, tuple):
            self.x = x
            self.y = y
            self.image = image
            self.name = name
            self.location = location
        else:
            raise TypeError("One or more arguments dont macth type.\n X & Y must be int, image and name must be str and location must be a tuple")

    def getX(self):
        return self.x

    def setX(self, value):
        if isinstance(value, int):
            self.x = value
        else:
            raise TypeError("value must be a int")

    def getY(self):
        return self.y

    def setY(self, value):
        if isinstance(value, int):
            self.y = value
        else:
            raise TypeError("value must be a int")

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
