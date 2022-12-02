import sys, os
import unittest

from days.day_01 import DayOne

class TestDayOne(unittest.TestCase):
    # https://adventofcode.com/2022/day/1

    test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    def test_find_max_sum(self):
        with open("test_input", "w") as f:
            f.write(self.test_input)
        d = DayOne()
        actual = d.part_one("./test_input")
        self.assertEqual(actual, 24000)

        os.remove('./test_input')

    def test_find_top_three_max_sums(self):
        with open("test_input", "w") as f:
            f.write(self.test_input)
        d = DayOne()
        actual = d.part_two("./test_input")
        self.assertEqual(actual, 45000)

        os.remove('./test_input')
        
if __name__ == '__main__':
    unittest.main()