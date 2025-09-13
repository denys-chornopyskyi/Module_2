from datetime import datetime
import os
import json
from abc import ABC, abstractmethod
 
from .settings import RESULTS_FILE


class DataStorage(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class FileCheckMixin():
    def _ensure_file_exists(self, file_path, file_text=''):
        if not os.path.exists(file_path):
            with open(file_path, 'x', encoding='utf-8') as f:
                f.write(file_text)


class JSONDataStorage(DataStorage, FileCheckMixin):
    def __init__(self, filename):
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, filename))

    def save(self, result):
        self._ensure_file_exists(self.path, '[]')
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

    def load(self):
        self._ensure_file_exists(self.path, '[]')
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)
        

class JSONResultStorage(JSONDataStorage):
    def __init__(self, filename):
        super().__init__(filename)

    def save(self, player_name, rounds_played, final_score):
        result = {
                "Дата": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "Игрок": player_name,
                "Количество раундов": rounds_played,
                "Итоговый счет": final_score
            } 
        results = super().load()
        results.append(result)
        super().save(results)

    def load(self):
        results = super().load()
        for result in results:
             print('-------------------------------')
             print(f"Дата: {result['Дата']}")
             print(f"Игрок: {result['Игрок']}")
             print(f"Количество раундов: {result['Количество раундов']}")
             print(f"Итоговый счет: {result['Итоговый счет']}")


if __name__ == '__main__':
    pass
