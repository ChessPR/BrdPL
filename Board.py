import numpy as np
from tkinter import *


class Board(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def createPlainGrid(self, color):
        gameboard = np.zeros((self.x, self.y))
        color_Arr = [color]
        return [gameboard, color_Arr]

    def createChessBoard(self, color1, color2):
        print(self.x)
        print(self.y)
        gameboard = np.zeros((self.x, self.y))
        gameboard[1::2, 0::2] = 1
        gameboard[0::2, 1::2] = 1
        color_Arr = [color1, color2]
        return [gameboard, color_Arr]

    def display(self,  np, width, height, color_Arr):
        window = Tk()
        thecanvas = Canvas(window, width=width, height=height)
        thecanvas.grid(row=0, column=0, columnspan=2)
        window.update_idletasks()
        w = width / self.x
        h = height / self.y
        for row in range(self.x):
            for col in range(self.y):
                fillcolor = color_Arr[int(np[row, col])]
                thecanvas.create_rectangle(col*w, row*h, (col+1)*w, (row+1)*h, fill=fillcolor)
        window.mainloop()

board = Board(8, 8)
b = board.createChessBoard("white", "black")
# print(b)
# print(b[0, 1])
# print(b[0, 2])
# board.display(b, 750, 750, "#F8F8FF", "#A0522D")
print(b[0])
print(b[1])
board.display(b[0], 750, 750, b[1])

