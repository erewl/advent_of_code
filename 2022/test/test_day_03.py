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

    def test_calculate_total_score_according_to_plan(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayThree()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 157)

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()