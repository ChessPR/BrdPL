from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from Piece import *
root = Tk()

root.geometry("800x800")

red = Piece('red.png', 'red Piece')
black = Piece('black.png', 'black Piece')

photo = red.createImage()
photo1 = black.createImage()
photo2 = PhotoImage(file='redQueen.png')
# for i in range (8):
#     if (i % 2 == 0):
#         label = Label(image=photo)
#         label.place(x=100*i, y=100*i)
#     else:
#         label = Label(image=photo1)
#         label.place(x=100*i, y=100*i)


arr = np.zeros((8, 8))
arr[1::2, 0::2] = 1
arr[0::2, 1::2] = 1
arr[0][2] = 2
arr[0][3] = 4
arr[3,0] = 3
photoArray = [photo, photo1, photo2]
colorArray = ['black', 'white']
print(arr)

def display(colorArray, photoArray):
    for row in range(8):
        for col in range(8):
            if int(arr[row][col]) == 0:
                label = Label(bg=colorArray[0], width=100, height=100)
                label.place(x=100*row, y=100*col)
            elif int(arr[row][col]) == 1:
                label = Label(bg=colorArray[1], width=100, height=100)
                label.place(x=100*row, y=100*col)
            else:
                label = Label(image=photoArray[int(arr[row][col]) - 2])
                label.place(x=100*row, y=100*col)
                # if arr[row, col] == 0:
                #     label = Label(image=photo)
                #     label.place(x=100*row, y=100*col)
                # elif arr[row, col] == 1:
                #     label = Label(image=photo1)
                #     label.place(x=100*row, y=100*col)
                # else:
                #     label = Label(image=photo2)
                #     label.place(x=100*row, y=100*col)
    root.mainloop()


display(colorArray, photoArray)
