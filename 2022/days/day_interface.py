from posixpath import split
from typing import Callable, Generic, TypeVar

# Generic since, the input format can vary from day to day
T = TypeVar('T')

class DayBaseClass:

    def part_one(self,  input_file: str)-> str:
        pass

    def part_two(self, input_file: str)-> str:
        pass

    def parse_input(self, input_file: str)-> Generic[T]:
        with open(input_file) as f:
            lines = f.read().split('\n')
            return lines