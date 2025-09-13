from abc import ABC, abstractmethod

from game import *

class MenuOption(ABC):
    
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class StartGame(MenuOption):
    def execute(self):
        player_name = input('Введите свое имя: ')
        player = Player(player_name)
        computer = Computer()
        storage = JSONResultStorage(RESULTS_FILE)
        selected_mode = choose_game_mode()
        game = GameSession(
            player=player, 
            opponent=computer, 
            storage=storage, 
            mode_name=selected_mode.title, 
            rounds=selected_mode.rounds
            )
        game.start()

    def __str__(self):
        return 'Играть.'


class LoadResults(MenuOption):
    def execute(self):
        JSONResultStorage(RESULTS_FILE).load()

    def __str__(self):
        return 'Посмотреть результаты.'


class Exit(MenuOption):
    def execute(self):
        exit()

    def __str__(self):
        return 'Выйти.'


def main():
    options_list: list[MenuOption] = [StartGame(), LoadResults(), Exit()]

    while True:
        for i, option in enumerate(options_list, 1):
            print(f'{i}. {option}')

        choice = int(get_valid_input('Выберите один из вариантов: ', RangeValidator(1, len(options_list))))

        selected_option = options_list[choice - 1]
        selected_option.execute()
        

if __name__ == '__main__':
    main()