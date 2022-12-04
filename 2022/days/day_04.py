from typing import List
from days.day_interface import DayBaseClass


class DayFour(DayBaseClass):

    def part_one(self, input_file: str) -> str:
        input = self.parse_input(input_file)
        return sum([1 for left, right in input if set(left).issubset(right) or set(right).issubset(left)])

    def part_two(self, input_file: str) -> str:
        input = self.parse_input(input_file)
        return sum([1 for left, right in input if not set(left).isdisjoint(right)])

    def parse_input(self, input_file: str) -> List[List[str]]:
        lines = super().parse_input(input_file)
        pairs = [line.split(',') for line in lines] 

        def create_range(i: str):
            f = [ int(c) for c in i.split('-')]
            if f[0] == f[1]:
                return [f[0]]
            return list(range(f[0], f[1]+1))

        return [[create_range(item) for item in pair] for pair in pairs]
         
        