from functools import reduce

class DayOne():

    def part_one(self, input_file):
        input = self.parse_instructions(input_file)
        sums = max([sum(i) for i in input])
        return sums

    def part_two(self, input_file):
        input = self.parse_instructions(input_file)
        sorted_sums = sorted([sum(i) for i in input])
        return sum(sorted_sums[-3:])

    def parse_instructions(self, input_file):
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
    