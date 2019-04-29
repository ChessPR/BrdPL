class Player(object):

    def __init__(self, name, turn, score):
        if isinstance(name, str) and isinstance(turn, bool) and isinstance(score, int or float):
            self.name = name
            self.turn = turn
            self.score = score
        else:
            raise TypeError("One or more arguments don't match the corresponding type")

    def addScore(self, score):
        if isinstance(score, int or float):
            self.score += score
        else:
            raise TypeError("The score must be int of float")

    def setScore(self, score):
        if isinstance(score, int or float):
            self.score = score
        else:
            raise TypeError("The score must be int of float")

    def changeTurn(self, turn):
        if isinstance(turn, bool):
            self.turn = turn
        else:
            raise TypeError("Turn must be a boolean")

    def changeName(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name must be a string")

    def print(self):
        print("Name: " + self.name + " Turn: " + str(self.turn) + " Score: " + str(self.score))
