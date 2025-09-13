from os import system

from .settings import display_dice 
from .models import Player
from .score import DataStorage
from .validators import EmptyStringValidator
from .game_utils import get_valid_input, print_result


class GameSession():
    def __init__(self, player: Player, opponent: Player, storage: DataStorage, mode_name : str, rounds: int):
        self.player = player
        self.opponent = opponent
        self.storage = storage
        self.mode_name = mode_name
        self.rounds = rounds
        self.diff = 0
        
    def start(self):
        current_round = 1
        
        system('clear')
        print(f'Игра началась! Режим: {self.mode_name}, количество раундов {self.rounds}')

        while 0 < current_round <= self.rounds:
            print('---------------------------------')
            print(f'Раунд {current_round}:')
            current_round += 1
            while True:
                self.player.score = self.player.roll_dice()
                self.opponent.score = self.opponent.roll_dice()

                get_valid_input('Кинуть кубик:', EmptyStringValidator())

                print(f'Вы бросили кубик: {self.player.score}')
                display_dice(self.player.score)
                

                print(f'Компьютер бросил кубик: {self.opponent.score}')
                display_dice(self.opponent.score)

                self.diff = self.diff + self.player.score - self.opponent.score
                print(f'Разница: {self.diff}')

                if self.player.score != self.opponent.score:
                    break
                print('перебрасывание кубиков')

        
        print_result(self.player.name, self.mode_name, self.diff)
        self.storage.save(self.player.name, self.rounds, self.diff)


    