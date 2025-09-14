from random import randint

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def roll_dice(self):
        return randint(1, 6)
		

class Computer(Player):
    def __init__(self):
        super().__init__('Computer')
     