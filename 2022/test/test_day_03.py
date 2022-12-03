import unittest, os

from days.day_03 import DayThree



class TestDayThree(unittest.TestCase):
    # https://adventofcode.com/2022/day/3

    test_input_file_path = './test/test_input'

    test_input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

    def test_find_common_item_between_two_compartments(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayThree()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 157)

        os.remove(self.test_input_file_path)

    def test_find_common_item_between_three_rucksacks(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayThree()
        actual = d.part_two(self.test_input_file_path)
        self.assertEqual(actual, 70)

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()