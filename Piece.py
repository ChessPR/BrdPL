from tkinter import *
from PIL import ImageTk, Image


class Piece(object):

    def __init__(self, x, y, image, name):
        self.x = x
        self.y = y
        self.image = image
        self.name = name

    def make(self):
        i = self.image
        self.image = ImageTk.PhotoImage(Image.open(i))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImage(self):
        return self.image

    def getName(self):
        return self.name

