from typing import List
from days.day_interface import DayBaseClass


class DayEight(DayBaseClass):

    def _transpose_matrix(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    def part_one(self, input_file: str) -> int:
        def is_tree_visible_at_position(x: int, y: int, matrix: List[List[int]], transposed_matrix: List[List[int]]) -> bool:
            tree_height = matrix[x][y]
            left_row = matrix[x][0:y]
            right_row = matrix[x][y+1::]
            top_row = transposed_matrix[y][0:x]
            bottom_row = transposed_matrix[y][x+1::]

            return \
                all(i < tree_height for i in left_row) or \
                all(i < tree_height for i in right_row) or \
                all(i < tree_height for i in top_row) or \
                all(i < tree_height for i in bottom_row)

        matrix = self.parse_input(input_file)
        transposed_matrix = self._transpose_matrix(matrix)
        visible_trees = [tree for row_index, tree_row in enumerate(matrix[1:-1], 1) for tree_index, tree in enumerate(
            tree_row[1:-1], 1) if is_tree_visible_at_position(row_index, tree_index, matrix, transposed_matrix)]
        return len(visible_trees) + len(matrix[0])*2 + (len(matrix)-2)*2

    def part_two(self, input_file: str) -> int:
        matrix = self.parse_input(input_file)

        def get_scenic_score_of_tree_at_position(x: int, y: int, matrix: List[List[int]], transposed_matrix: List[List[int]]) -> int:
            tree_height = matrix[x][y]
            left_row = matrix[x][0:y]
            right_row = matrix[x][y+1::]
            top_row = transposed_matrix[y][0:x]
            bottom_row = transposed_matrix[y][x+1::]

            def count_visible_trees(tree_row, tree) -> int:
                count = 0
                for t in tree_row:
                    if t < tree:
                        count += 1
                    if t >= tree:
                        return count+1
                return count

            top_row.reverse() 
            left_row.reverse()
            return \
                count_visible_trees(left_row, tree_height) * \
                count_visible_trees(right_row, tree_height) * \
                count_visible_trees(top_row, tree_height) * \
                count_visible_trees(bottom_row, tree_height)
        matrix = self.parse_input(input_file)
        transposed_matrix = self._transpose_matrix(matrix)

        f = [get_scenic_score_of_tree_at_position(x, y, matrix, transposed_matrix) for x in range(1, len(matrix[1:-1][0])) for y in range(1, len(matrix[1:-1]))]
        return max(f)

    def parse_input(self, input_file: str) -> dict:
        lines = super().parse_input(input_file)
        return [[int(tree)for tree in line] for line in lines]
