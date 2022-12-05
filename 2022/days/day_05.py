from functools import reduce
from re import S
from typing import List
from days.day_interface import DayBaseClass


class DayFive(DayBaseClass):

    def _execute_instruction(self, cargo_plan: dict, instruction: List[int], reverse_stack_order: bool = True) -> dict:
        amount, source, target = instruction
        source_row = cargo_plan[source]
        target_row = cargo_plan[target]
        a = source_row[-amount:]
        if reverse_stack_order:
            a.reverse()
        cargo_plan.update(
            {source: source_row[:-amount], target: target_row + a})
        return cargo_plan

    def part_one(self, input_file: str) -> str:
        starting_cargo_plan, moving_instructions = self.parse_input(input_file)

        f = reduce(lambda cargo_plan, current_instructions: self._execute_instruction(
            cargo_plan, current_instructions), moving_instructions, starting_cargo_plan)
        message = [a[-1] for a in f.values() if len(a) > 0]
        return ''.join(message)

    def part_two(self, input_file: str) -> str:
        starting_cargo_plan, moving_instructions = self.parse_input(input_file)

        f = reduce(lambda cargo_plan, current_instructions: self._execute_instruction(
            cargo_plan, current_instructions, reverse_stack_order=False), moving_instructions, starting_cargo_plan)
        message = [a[-1] for a in f.values() if len(a) > 0]
        return ''.join(message)

    def parse_input(self, input_file: str):
        with open(input_file, 'r') as f:
            input = f.read()
            plan_raw, instructions_raw = input.split('\n\n')

            def create_dict(cargo_plan: dict, crates: List[str]) -> dict:
                crates_dict = {index+1: cargo_plan[index + 1] + [crate]
                               for index, crate in enumerate(crates) if not crate == ''}
                cargo_plan.update(crates_dict)
                return cargo_plan

            def parse_plan(raw: str) -> dict:
                lines = raw.split('\n')
                crates_arrangement = lines[:-1]
                crates_arrangement.reverse()
                row_numbers = [
                    int(row_number) for row_number in lines[-1].split(' ') if not row_number == '']

                crates_arrangement = [i.replace('    ', ' ').replace(
                    '[', '').replace(']', '').split(' ') for i in crates_arrangement]

                empty_cargo_plan = {number: [] for number in row_numbers}

                return reduce(lambda acc, curr: create_dict(acc, curr), crates_arrangement, empty_cargo_plan)

            plan = parse_plan(plan_raw)
            instructions = [[int(l) for l in line.split(' ') if l.isdigit()]
                            for line in instructions_raw.split('\n')]
            return plan, instructions
