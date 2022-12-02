import unittest, os

from days.day_02 import DayTwo


class TestDayOne(unittest.TestCase):

    test_input_file_path = './test/test_input'

    test_input = '''A Y
B X
C Z'''

    def test_calculate_score(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayTwo()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 15)

        os.remove(self.test_input_file_path)


if __name__ == '__main__':
    unittest.main()