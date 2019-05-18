from Board import *
from Piece import *
from Dice import *
from Player import *

# Board
board = Board(8, 8, window=Tk())

# Dice
d = Dice(2, 6)

# Pieces
red = Piece('red.png', 'red Piece').createImage()
black = Piece('black.png', 'black Piece').createImage()
redQueen = Piece('redQueen.png', 'red Queen').createImage()
blackQueen = Piece('blackQueen.png', 'black Queen').createImage()

# Players
player1 = Player('Wilson', False, 0, 1)
player2 = Player('Estudiante', False, 0, 2)

# Board attributes
pieceArr = [red, black, redQueen, blackQueen]
b = board.createCheckerStart('white', 'black', pieceArr)
board.display(b[0], 800, 800, b[1], b[2])
board.getWindow().mainloop()


# def move(npArray, piece, startPos, endPos, player):
#     global board
#     if isLegal(npArray, piece, startPos, endPos, player):
#         npArray[startPos[0], startPos[1]] = npArray[endPos[0], endPos[1]]
#
#
# def isLegal(npArray, piece, startPos, endPos, player):
#     if piece < 4 and player == 1:
#         p1 = [startPos[0] - 1, startPos[1] + 1]
#         p2 = [startPos[0] - 1, startPos[1] - 1]
#         # endPos is not legal
#         if endPos != p1 and endPos != p2:
#             return print("Invalid move")
#         # Same piece in the possible move
#         if p1 == piece and p2 == piece:
#             return print("Invalid move")
#
#     if piece < 4 and player == 2:
#         p1 = [startPos[0] + 1, startPos[1] + 1]
#         p2 = [startPos[0] + 1, startPos[1] - 1]
#         if endPos != p1 and endPos != p2:
#             return print("Invalid move")
#         # Same piece in the possible move
#         if p1 == piece and p2 == piece:
#             return print("Invalid move")
