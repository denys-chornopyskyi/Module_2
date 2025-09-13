from abc import ABC, abstractmethod

from .exceptions import InvalidNumberError, InvalidRollError


class Validator(ABC):
    
    @abstractmethod
    def validate(self, value: str):
        pass

        
class EmptyStringValidator(Validator):

    def validate(self, input: str) -> bool | Exception:
        if input.strip() == '':
            return True
        raise InvalidRollError


class NumValidator(Validator):

    def validate(self, input: str) -> bool | Exception:
        if input.isdigit():
            return True
        raise ValueError('nevernij vvod! vvedite cislo')


class RangeValidator(NumValidator):
    
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val;
        self.max_val = max_val;

    def validate(self, value: str) -> bool | Exception:
        super().validate(value)
        if self.min_val <= int(value) <= self.max_val:
            return True
        raise InvalidNumberError(value, self.min_val, self.max_val)
