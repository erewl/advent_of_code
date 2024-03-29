from functools import reduce
from typing import List

from days.day_interface import DayBaseClass

class DayOne(DayBaseClass):

    def part_one(self, input_file):
        input = self.parse_input(input_file)
        sums = max([sum(i) for i in input])
        return sums

    def part_two(self, input_file):
        input = self.parse_input(input_file)
        sorted_sums = sorted([sum(i) for i in input])
        return sum(sorted_sums[-3:])

    def parse_input(self, input_file)-> List[List[int]]:
        def parse_input(acc, curr):
            if curr == '':
                acc.append([])
                return acc
            else:
                i = int(curr)
                acc[-1].append(i)
                return acc

        with open(input_file, "r") as f:
            input = f.read().split("\n")
            i = reduce(lambda acc, curr: parse_input(acc,curr), input, [[]])
            return i
    