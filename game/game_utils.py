from datetime import datetime
from os import system

from .validators import Validator, RangeValidator
from .settings import GameLevel

def get_valid_input(prompt: str, *validators: Validator):
        while True:
            try:
                value = input(prompt)
                for validator in validators:
                    validator.validate(value)
                return value
            except Exception as e:
                print(e)

def choose_game_mode() -> GameLevel:
    print('Выберите режим игры:')

    for i, mode in enumerate(GameLevel, 1):
        print(f'{i}. {mode.title} ({mode.value} раундов)')

    choice = get_valid_input('Введите номер режима: ', RangeValidator(1, len(GameLevel)))
    return list(GameLevel)[int(choice) - 1]
    
def print_result(player_name, game_mode, final_score):
    system('clear')
    print(f"Вы {'выграли!!' if final_score > 0 else 'проиграли!!'}")
    print(f"Время:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Игрок: {player_name}")
    print(f"Режим: {game_mode}")
    print(f"Итоговый счет: {final_score}")
