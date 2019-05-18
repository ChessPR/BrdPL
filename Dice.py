import random as r


class Dice(object):

    def __init__(self, number_of_dices, sides):
        self.number_of_dices = number_of_dices
        self.sides = sides

    def roll(self):
        arr = []
        for i in range (self.number_of_dices):
            arr.append(r.randint(1, self.sides))
        return arr


# For testing purposes
# dice = Dice(2, 6)
# dice.roll()
