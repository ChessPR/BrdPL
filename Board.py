import numpy as np
from tkinter import *
from PIL import ImageTk , Image
from Piece import *


class Board(object):

    def __init__(self, x, y, window):
        if isinstance(x and y, int):
            self.x = x
            self.y = y
            self.window = window
        else:
            raise TypeError("You must enter two integers specifying the dimensions of the 2d board")

    def createPlainGrid(self, color):
        if isinstance(color, str):
            gameboard = np.zeros((self.x, self.y))
            color_Arr = [color]
            return [gameboard, color_Arr]
        else:
            raise TypeError("Color must be a string")

    def createCheckerStart(self, color1, color2, pieceArr):
        gameboard = np.zeros((self.x, self.y))
        gameboard[1::2, 0::2] = 1
        gameboard[0::2, 1::2] = 1
        for row in range(8):
            for col in range(3):
                if gameboard[row, col] == 1:
                    gameboard[row, col] = 2

        for row in range(8):
            for col in range(3):
                if gameboard[row, col+5] == 1:
                    gameboard[row, col+5] = 3
        colorArr = [color1, color2]
        return [gameboard, colorArr, pieceArr]

    def createChessBoard(self, color1, color2, pieceArr):
        for p in pieceArr:
            if isinstance(p and color1 and color2, str):
                pass
            else:
                raise TypeError("Colors must be strings")
        gameboard = np.zeros((self.x, self.y))
        gameboard[1::2, 0::2] = 1
        gameboard[0::2, 1::2] = 1
        colorArr = [color1, color2]
        return [gameboard, colorArr, pieceArr]

    def display(self,  arr, width, height, color_Arr, piece_Arr):
        if isinstance(color_Arr, list) and isinstance(width and height, int) and isinstance(arr, np.ndarray):
            self.window.geometry(str(width) + "x" + str(height))
            x = int(width/self.x)
            y = int(height/self.y)
            for row in range(self.x):
                for col in range(self.y):
                    if int(arr[row, col]) == 0:
                        label = Label(bg=color_Arr[0], width=x, height=y)
                        label.place(x=row*x, y=col*y)
                    elif int(arr[row, col]) == 1:
                        label = Label(bg=color_Arr[1], width=x, height=y)
                        label.place(x=row*x, y=col*y)
                    else:
                        label = Label(image=piece_Arr[int(arr[row, col] - 2)])
                        label.place(x=row*x, y=col*y)
            self.window.mainloop()
        else:
            raise TypeError("One or more arguments have the wrong type")

    def getWindow(self):
        return self.window

# For testing purposes
#
# # board = Board(8, 8, window=Tk())
# board = Board(8, 8, window=Tk())
# red = Piece('red.png', 'red Piece').createImage()
# black = Piece('black.png', 'black Piece').createImage()
# redQueen = Piece('redQueen.png', 'red Queen').createImage()
# blackQueen = Piece('blackQueen.png', 'black Queen').createImage()
#
# # pieceArr = [red, black, redQueen, blackQueen]
# #
# # b = board.createChessBoard("white", "black", pieceArr)
# #
# # board.display(b[0], 800, 800, b[1], b[2])
#
# # print(type(b))
# # print(b[0, 1])
# # print(b[0, 2])
# # board.display(b, 750, 750, "#F8F8FF", "#A0522D")
# # print(type(b[0]))
# # print(type(b[1]))
#
# pieceArr = [red, black, redQueen, blackQueen]
# b = board.createCheckerStart('white', 'black', pieceArr)
# board.display(b[0], 800, 800, b[1], b[2])
