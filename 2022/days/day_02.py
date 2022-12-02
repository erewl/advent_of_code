
from typing import List
from days.day_interface import DayBaseClass


class DayTwo(DayBaseClass):

    __score_mapping_for_choice = {
        'A': 1,
        'X': 1,
        'B': 2,
        'Y': 2,
        'C': 3,
        'Z': 3
    }

    def __is_win(self, you: str, opponent: str) -> bool:
        return \
            you == 'X' and opponent == 'C' or \
            you == 'Y' and opponent == 'A' or \
            you == 'Z' and opponent == 'B'

    def __is_draw(self, you: str, opponent: str) -> bool:
        # swap you and opponent order, since at a draw the order doesnt matter and simplifies the statement
        you, opponent = [opponent, you] if opponent in 'ABC' else [you, opponent]
        return \
            you == 'A' and opponent == 'X' or \
            you == 'B' and opponent == 'Y' or \
            you == 'C' and opponent == 'Z'

    def part_one(self, input_file: str) -> str:
        rounds = self.parse_input(input_file)

        def calculate_score_in_round(round: List[str]) -> int:
            opponent, you = round
            initial_score = self.__score_mapping_for_choice[you]
            if self.__is_win(you, opponent):
                return 6 + initial_score
            if self.__is_draw(you, opponent):
                return 3 + initial_score
            else:
                return 0 + initial_score

        return sum([calculate_score_in_round(round) for round in rounds])

    def part_two(self, input_file: str) -> str:
        return super().part_two(input_file)

    def parse_input(self, input_file: str) -> List[List[str]]:
        with open(input_file, 'r') as f:
            lines = f.read()
            return [line.split(' ') for line in lines.split('\n')]
