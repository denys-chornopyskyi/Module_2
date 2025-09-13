class InvalidNumberError(Exception):
    def __init__(self, value, min_num=1, max_num=3):
        self.value = value
        self.min_num = min_num
        self.max_num = max_num
        super().__init__(f'Error!! cislo {self.value} vne diapazona {self.min_num} - {self.max_num}')


class InvalidRollError(Exception):
    def __init__(self):
        super().__init__(f'Бросок не сделан!!! Нажмите "Enter" для повторного броска.')

 