import random


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


for i in range(11):
    d = Die(10)
    d.roll_die()
