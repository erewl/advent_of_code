import unittest, os

from days.day_05 import DayFive



class TestDayFive(unittest.TestCase):
    # https://adventofcode.com/2022/day/5

    test_input_file_path = './test/test_input'

    test_input = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

    def test_1(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayFive()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 'CMZ')

        os.remove(self.test_input_file_path)

    def test_2(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DayFive()
        actual = d.part_two(self.test_input_file_path)
        self.assertEqual(actual, 'MCD')

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()