import unittest, os

from days.day_08 import DayEight



class TestDayEight(unittest.TestCase):
    # https://adventofcode.com/2022/day/8

    test_input_file_path = './test/test_input'

    test_input = '''30373
25512
65332
33549
35390'''

    def test_1(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayEight()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 21)

        os.remove(self.test_input_file_path)

    def test_2(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayEight()
        actual = d.part_two(self.test_input_file_path)
        self.assertEqual(actual, 8)

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()