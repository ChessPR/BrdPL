from tkinter import *
from PIL import ImageTk, Image
import numpy as np

root = Tk()

root.geometry("800x800")

photo = PhotoImage(file='black.png')
photo1 = PhotoImage(file='red.png')
photo2 = PhotoImage(file='redQueen.png')
# for i in range (8):
#     if (i % 2 == 0):
#         label = Label(image=photo)
#         label.place(x=100*i, y=100*i)
#     else:
#         label = Label(image=photo1)
#         label.place(x=100*i, y=100*i)


arr = np.zeros((8,8))
arr[1::2, 0::2] = 1
arr[0::2, 1::2] = 1
arr[0][2] = 2
photoArray = [photo, photo1, photo2]
def display(photoArray):
    for row in range(8):
        for col in range(8):
            label = Label(image=photoArray[int(arr[row][col])])
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


display(photoArray)
