from PIL import Image
from tkinter import *


class Piece(object):

    def __init__(self, image, name):
        if isinstance(image and name, str):
            self.image = image
            self.name = name
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

    def createImage(self):
        return PhotoImage(file=self.image)
