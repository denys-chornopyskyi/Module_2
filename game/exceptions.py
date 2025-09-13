class OutOfRangeError(Exception):
    """raises when a number is out of allowed range"""

    def __init__(self, value, min_num=1, max_num=3):
        self.value = value
        self.min_num = min_num
        self.max_num = max_num
        super().__init__(f"Ошибка! Число {self.value} вне допустимого диапазона "
                        f"от {self.min_num} до {self.max_num}.")


class InvalidRollError(Exception):
    """raises when a dice roll fails"""

    def __init__(self):
        super().__init__(f'Бросок не сделан!!! Нажмите "Enter" для повторного броска.')

 