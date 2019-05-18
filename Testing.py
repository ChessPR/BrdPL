import numpy as np
from tkinter import *
from PIL import ImageTk , Image
import Piece


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
            for row in range(self.x):
                for col in range(self.y):
                        im = piece_Arr[int(arr[row, col]) - 2]
                        photo = PhotoImage(file=im)
                        label = Label(image=photo)
                        label.place(x=col*width/self.x, y=row*height/self.y)
            self.window.mainloop()
        else:
            raise TypeError("One or more arguments have the wrong type")


# For testing purposes

board = Board(8, 8, window=Tk())
pieceArr = ['black.png', 'red.png', 'blackQueen.png', 'redQueen.png']
b = board.createChessBoard("white", "black", pieceArr)
# print(type(b))
# print(b[0, 1])
# print(b[0, 2])
# board.display(b, 750, 750, "#F8F8FF", "#A0522D")
# print(type(b[0]))
# print(type(b[1]))
if isinstance(b[0], np.ndarray):
    print("Its ok")

b[0][4][0] = 3
b[0][0][0] = 3
# a[0, 7] = 4
# a[0, 2] = 2
# a[5, 0] = 2
# a[7, 7] = 4
print(b[0])

# im = PhotoImage(file='chessKing.png')
board.display(b[0], 800, 800, b[1], b[2])









            #
            # for pieces in ArrPieces:
            #     img = Image.open(pieces.image).resize((pieces.x, pieces.y), Image.ANTIALIAS)
            #     picture = ImageTk.PhotoImage(img)
            #     pic = Label(thecanvas, image=picture)
            #     pic.place(x=pieces.location[0], y=pieces.location[1])
            #     labelArr.append(pic)
