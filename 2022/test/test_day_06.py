import unittest, os

from days.day_06 import DaySix



class TestDaySix(unittest.TestCase):
    # https://adventofcode.com/2022/day/6

    test_input_file_path = './test/test_input'

    test_input = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

    def test_find_non_repeating_sequence_after_how_many_characters(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DaySix()
        actual = d.part_one(self.test_input_file_path)
        self.assertEqual(actual, 7)

        os.remove(self.test_input_file_path)

    def test_2(self):
        with open(self.test_input_file_path, "w") as f:
            f.write(self.test_input)

        d = DaySix()
        actual = d.part_two(self.test_input_file_path)
        self.assertEqual(actual, 19)

        os.remove(self.test_input_file_path)

if __name__ == '__main__':
    unittest.main()