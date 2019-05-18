import numpy as np
from tkinter import *
from PIL import Image
import Piece


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
        count = 0
        if isinstance(color_Arr, list) and isinstance(width and height, int) and isinstance(arr, np.ndarray):
            window = Tk()
            thecanvas = Canvas(window, width=width, height=height)
            thecanvas.grid(row=0, column=0, columnspan=2)
            window.update_idletasks()
            w = width / self.x
            h = height / self.y
            # Color game board
            for row in range(self.x):
                for col in range(self.y):
                        if count % 9 == 8:
                            count = count + 1
                        fillcolor = color_Arr[count % 2]
                        count = count + 1
                        if arr[row, col] != 0 and arr[row, col] != 1:
                            print(a[row, col])
                            im = int(arr[row, col])
                            im = piece_Arr[im - 2]
                            im = createImage(im)
                            if row == 0 and col == 0:
                                createImage(im, width/(2*self.x), height/(2*self.y))
                                # thecanvas.create_image(width/(2*self.x), height/(2*self.y), image=im)
                            elif row == 0:
                                createImage(im, col*width/(2*self.x) + width/self.x, height/self.x)
                                # thecanvas.create_image(col*width/(2*self.x) + width/self.x, height/self.x, image=im)
                            elif col == 0:
                                createImage(im, height/(2*self.y), row*height/(2*self.y) + height/self.y)
                                # thecanvas.create_image(height/(2*self.y), row*height/(2*self.y) + height/self.y, image=im)
                            else:
                                createImage(im, col*width/self.x + width/(2*self.x), row*height/self.y + height/(2*self.y))
                                # thecanvas.create_image(col*width/self.x + width/(2*self.x), row*height/self.y + height/(2*self.y), image=im)
                        else:
                            thecanvas.create_rectangle(col*w, row*h, (col+1)*w, (row+1)*h, fill=fillcolor)
            #
            # # Put images
            # for row in range(self.x):
            #     for col in range(self.y):
            #         if arr[row, col] != 0 and arr[row, col] != 1:
            #             print(a[row, col])
            #             im = int(arr[row, col])
            #             im = piece_Arr[im - 2]
            #             im = createImage(im)
            #             if row == 0 and col == 0:
            #                 thecanvas.create_image(width/(2*self.x), height/(2*self.y), image=im)
            #             elif row == 0:
            #                 thecanvas.create_image(col*width/(2*self.x) + width/self.x, height/self.x, image=im)
            #             elif col == 0:
            #                 thecanvas.create_image(height/(2*self.y), row*height/(2*self.y) + height/self.y, image=im)
            #             else:
            #                 thecanvas.create_image(col*width/self.x + width/(2*self.x), row*height/self.y + height/(2*self.y), image=im)
            #         else:
            #             pass
            window.mainloop()
        else:
            raise TypeError("One or more arguments have the wrong type")


# def createImage(image, x, y):

def createCanvas(window, width, height):
    return Canvas(Canvas(window, width=width, height=height))


# For testing purposes
# board = Board(8, 8)
# pieceArr = ['black.png', 'red.png', 'blackQueen.png', 'redQueen.png']
# b = board.createChessBoard("white", "black", pieceArr)
# # print(type(b))
# # print(b[0, 1])
# # print(b[0, 2])
# # board.display(b, 750, 750, "#F8F8FF", "#A0522D")
# # print(type(b[0]))
# # print(type(b[1]))
# if isinstance(b[0], np.ndarray):
#     print("Its ok")
# print(b[0])
# print(b[1])
#
# a = b[0]
# a[1, 0] = 2
# a[0, 0] = 4
# print(b[0])
#
# # im = PhotoImage(file='chessKing.png')
# board.display(b[0], 800, 800, b[1], b[2])
#
#
#






            #
            # for pieces in ArrPieces:
            #     img = Image.open(pieces.image).resize((pieces.x, pieces.y), Image.ANTIALIAS)
            #     picture = ImageTk.PhotoImage(img)
            #     pic = Label(thecanvas, image=picture)
            #     pic.place(x=pieces.location[0], y=pieces.location[1])
            #     labelArr.append(pic)
