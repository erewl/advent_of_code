from typing import List
from days.day_interface import DayBaseClass


class DayThree(DayBaseClass):

    def part_one(self, input_file: str) -> str:
        rucksacks = self.parse_input(input_file)
        double_items = [set(left).intersection(right).pop() for left, right in rucksacks]

        def get_score(item: str):
            """
            Uses the unicode of a char to determine the score
            
            a-z have the scores 1-26, ord(a) = 97, therefore we need to use the offset 96 to determine their score
            
            A-Z have the scores 27-52, ord(A) = 65, therefore we need to use the offset 38 to determine their score
            """
            if item.isupper(): return ord(item) - 38
            else: return ord(item) - 96

        return sum([get_score(item) for item in double_items])

    
    def part_two(self, input_file: str) -> str:
        return super().part_two(input_file)
    
    def parse_input(self, input_file: str) -> List[List[str]]:
        lines: List[str] = super().parse_input(input_file)
        return [[line[:len(line)//2], line[len(line)//2:]] for line in lines] # split into two equal parts
        