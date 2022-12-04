import unittest, os

from days.day_04 import DayFour



class TestDayFour(unittest.TestCase):
    # https://adventofcode.com/2022/day/4

    test_input_file_path = './test/test_input'

    test_input = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

    def test_range_being_fully_contained_by_another_range(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayFour()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 2)

        os.remove(self.test_input_file_path)

    def test_range_overlapping_with_another_range(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayFour()
        actual = d.part_two(self.test_input_file_path)
        self.assertEqual(actual, 4)

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()