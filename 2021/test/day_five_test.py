
import sys
import unittest
sys.path.insert(0, '/Users/katringrunert/Projects/personal/advent_of_code_2021')

from days.day_five import *


class TestDrawLineMethods(unittest.TestCase):

    def test_orthogonal(self):
        a = [9, 9]
        b = [9, 5]
        self.assertEqual(draw_line(a,b), [(9,5),(9,6), (9,7), (9,8), (9,9)])
        self.assertEqual(draw_line(b,a), [(9,5),(9,6), (9,7), (9,8), (9,9)])

    def test_verticals(self):
        a = [3, 3]
        b = [1, 1]
        self.assertEqual(draw_line(a,b), [(3,3), (2,2), (1,1)])
        self.assertEqual(draw_line(b,a), [(1,1), (2,2), (3,3)])

        a = [9, 7]
        b = [7, 9]
        self.assertEqual(draw_line(a,b), [(9,7), (8,8), (7,9)])
        self.assertEqual(draw_line(b,a), [(7,9), (8,8), (9,7)])
        a= [5,5] 
        b = [8,2]
        self.assertEqual(draw_line(a,b), [(5,5), (6,4), (7,3), (8,2)])

        a= [6,4] 
        b = [2,0]
        self.assertEqual(draw_line(a,b), [(6,4), (5,3), (4,2), (3,1), (2,0)])


if __name__ == '__main__':
    unittest.main()
