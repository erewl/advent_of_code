from typing import List
from days.day_interface import DayBaseClass


class DayThree(DayBaseClass):

    def _get_score(self, item: str):
        """
        Uses the unicode of a char to determine the score
        
        a-z have the scores 1-26, ord(a) = 97, therefore we need to use the offset 96 to determine their score
        
        A-Z have the scores 27-52, ord(A) = 65, therefore we need to use the offset 38 to determine their score
        """
        if item.isupper(): return ord(item) - 38
        else: return ord(item) - 96

    def part_one(self, input_file: str) -> str:
        rucksacks = self.parse_input(input_file)
        rucksacks_compartements = [[rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]] for rucksack in rucksacks] # split into two equal parts
        double_items = [set(left).intersection(right).pop() for left, right in rucksacks_compartements]

        return sum([self._get_score(item) for item in double_items])

    
    def part_two(self, input_file: str) -> str:
        rucksacks = self.parse_input(input_file)
        group_size = 3
        grouped_rucksacks = [rucksacks[i:i + group_size] for i in range(0, len(rucksacks), group_size)]
        shared_items = [set(one).intersection(two).intersection(three).pop() for one,two,three in grouped_rucksacks]

        return sum([self._get_score(item) for item in shared_items])
    
    def parse_input(self, input_file: str) -> List[str]:
        return super().parse_input(input_file)
        