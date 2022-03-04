from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        len_row = len(matrix[0])
        for row in matrix:
            if len(row) != len_row:
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        return "\n".join([f'| {" ".join(map(str, row))} |' for row in self.matrix])

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('Матрицы должны быть одного размера!')
        return Matrix([list(map(sum, zip(row_1, row_2)))
                       for row_1, row_2 in zip(self.matrix, other.matrix)])


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])