import numpy as np
from tkinter import *
from Piece import *


class Board(object):

    def __init__(self, x, y):
        if isinstance(x and y, int):
            self.x = x
            self.y = y
        else:
            raise TypeError("You must enter two integers specifying the dimensions of the 2d board")

    def createPlainGrid(self, color):
        if isinstance(color, str):
            gameboard = np.zeros((self.x, self.y))
            color_Arr = [color]
            return [gameboard, color_Arr]
        else:
            raise TypeError("Color must be a string")

    def createChessBoard(self, color1, color2):
        if isinstance(color1, str) and isinstance(color2, str):
            gameboard = np.zeros((self.x, self.y))
            gameboard[1::2, 0::2] = 1
            gameboard[0::2, 1::2] = 1
            color_Arr = [color1, color2]
            return [gameboard, color_Arr]
        else:
            raise TypeError("Colors must be strings")

    def display(self,  arr, width, height, color_Arr, ArrPieces):
        if isinstance(color_Arr, list) and isinstance(width and height, int) and isinstance(arr, np.ndarray):
            window = Tk()
            thecanvas = Canvas(window, width=width, height=height)
            thecanvas.grid(row=0, column=0, columnspan=2)
            window.update_idletasks()
            w = width / self.x
            h = height / self.y
            for row in range(self.x):
                for col in range(self.y):
                    fillcolor = color_Arr[int(arr[row, col])]
                    thecanvas.create_rectangle(col*w, row*h, (col+1)*w, (row+1)*h, fill=fillcolor)
            # for pieces in ArrPieces:
            #     pieces
            #     thecanvas.create_image()
            window.mainloop()
        else:
            raise TypeError("One or more arguments have the wrong type")


# For testing purposes
board = Board(8, 8)
b = board.createChessBoard("white", "black")
print(type(b))
# print(b[0, 1])
# print(b[0, 2])
# board.display(b, 750, 750, "#F8F8FF", "#A0522D")
print(type(b[0]))
print(type(b[1]))
if isinstance(b[0], np.ndarray):
    print("Its ok")
img = "chessKing.png"
piece = Piece(20, 20, img, "King")
piece.make()
pieces = [piece]
print(pieces[0])
board.display(b[0], 750, 750, b[1], pieces)
