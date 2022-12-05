from functools import reduce
from typing import List
from days.day_interface import DayBaseClass


class DayFive(DayBaseClass):

    def _execute_moving_instruction(self, cargo_plan: dict, instruction: List[int], reverse_stack_order: bool = True) -> dict:
        amount, source, target = instruction
        source_stack = cargo_plan[source]
        target_stack = cargo_plan[target]
        popped_stack = source_stack[-amount:]
        if reverse_stack_order:  # when moving singular crates from A to B, this simulates the stack principle
            popped_stack.reverse()
        cargo_plan.update({
            source: source_stack[:-amount],
            target: target_stack + popped_stack
        })
        return cargo_plan

    def part_one(self, input_file: str) -> str:
        starting_cargo_plan, moving_instructions = self.parse_input(input_file)

        final_cargo_plan = reduce(
            lambda cargo_plan, current_instructions: self._execute_moving_instruction(
                cargo_plan, current_instructions),
            moving_instructions,
            starting_cargo_plan
        )
        last_crates_of_each_stack = [
            stack[-1] for stack in final_cargo_plan.values() if len(stack) > 0]
        return ''.join(last_crates_of_each_stack)

    def part_two(self, input_file: str) -> str:
        starting_cargo_plan, moving_instructions = self.parse_input(input_file)

        final_cargo_plan = reduce(
            lambda cargo_plan, current_instructions: self._execute_moving_instruction(
                cargo_plan, current_instructions, reverse_stack_order=False),
            moving_instructions,
            starting_cargo_plan
        )
        last_crates_of_each_stack = [
            stack[-1] for stack in final_cargo_plan.values() if len(stack) > 0]
        return ''.join(last_crates_of_each_stack)

    def parse_input(self, input_file: str):
        def fill_cargo_plan(cargo_plan: dict, crates: List[str]) -> dict:
            cargo_plan_update = {
                index: cargo_plan[index] + [crate]
                for index, crate in enumerate(crates, start=1) if not crate == ''
            }
            cargo_plan.update(cargo_plan_update)
            return cargo_plan

        def parse_plan(raw: str) -> dict:
            full_plan = raw.split('\n')
            stack_numbers, crates_arrangement = full_plan[-1].split(
                ' '), full_plan[:-1]
            crates_arrangement.reverse()
            stack_numbers = [
                int(stack_number) for stack_number in stack_numbers if not stack_number == '']

            crates_arrangement = [i.replace(4*' ', ' ')  # replace space-tabulated gaps by singular spaces for easier handling
                                  .replace('[', '')
                                  .replace(']', '').split(' ') for i in crates_arrangement]

            empty_cargo_plan: dict = {number: []
                                      for number in stack_numbers}
            return reduce(lambda acc, curr: fill_cargo_plan(acc, curr), crates_arrangement, empty_cargo_plan)

        with open(input_file, 'r') as f:
            input = f.read()
            plan_raw, instructions_raw = input.split('\n\n')

            cargo_plan = parse_plan(plan_raw)
            instructions = [[int(l) for l in line.split(' ') if l.isdigit()]
                            for line in instructions_raw.split('\n')]
            return cargo_plan, instructions
