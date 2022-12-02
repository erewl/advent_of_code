
from typing import List
from days.day_interface import DayBaseClass


class DayTwo(DayBaseClass):

    __score_mapping_for_choice = {
        'A': 1, 'X': 1,
        'B': 2, 'Y': 2,
        'C': 3, 'Z': 3
    }

    def part_one(self, input_file: str) -> str:
        """
        The input (X,Y,Z) indicates which choise should be made (Rock, Paper, Scissors).
        According to that choice, the score will be calculated
        """
        def is_win(you: str, opponent: str) -> bool:
            return \
                you == 'X' and opponent == 'C' or \
                you == 'Y' and opponent == 'A' or \
                you == 'Z' and opponent == 'B'

        def is_draw(you: str, opponent: str) -> bool:
            # swap you and opponent order, since at a draw the order doesnt matter and simplifies the statement
            you, opponent = [opponent, you] if opponent in 'ABC' else [
                you, opponent]
            return \
                you == 'A' and opponent == 'X' or \
                you == 'B' and opponent == 'Y' or \
                you == 'C' and opponent == 'Z'

        def calculate_score_in_round(round: List[str]) -> int:
            opponent, you = round
            initial_score = self.__score_mapping_for_choice[you]
            if is_win(you, opponent):
                return 6 + initial_score
            if is_draw(you, opponent):
                return 3 + initial_score
            else:
                return 0 + initial_score

        rounds = self.parse_input(input_file)
        return sum([calculate_score_in_round(round) for round in rounds])

    def part_two(self, input_file: str) -> str:
        """ 
        This time the input (X,Y,Z) gives us an indicator,
        whether we should win lose or draw against our opponent.
        According to that, the correct choice will be made (Rock, Paper, Scissors).
        """

        def determine_choice_for_loss(opponent: str) -> str:
            if opponent == 'A':
                return 'Z'
            if opponent == 'B':
                return 'X'
            else:
                return 'Y'

        def determine_choice_for_win(opponent: str) -> str:
            if opponent == 'A':
                return 'Y'
            if opponent == 'B':
                return 'Z'
            else:
                return 'X'

        def determine_choice_for_draw(opponent: str) -> str:
            if opponent == 'A':
                return 'X'
            if opponent == 'B':
                return 'Y'
            else:
                return 'Z'

        def calculate_score_in_round(round: List[str]) -> int:
            opponent, you = round
            if you == 'X':
                return 0 + self.__score_mapping_for_choice[determine_choice_for_loss(opponent)]
            if you == 'Y':
                return 3 + self.__score_mapping_for_choice[determine_choice_for_draw(opponent)]
            if you == 'Z':
                return 6 + self.__score_mapping_for_choice[determine_choice_for_win(opponent)]

        rounds = self.parse_input(input_file)
        return sum([calculate_score_in_round(round) for round in rounds])

    def parse_input(self, input_file: str) -> List[List[str]]:
        with open(input_file, 'r') as f:
            lines = f.read()
            return [line.split(' ') for line in lines.split('\n')]
