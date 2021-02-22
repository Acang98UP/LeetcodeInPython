from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    for i in range(len(matrix) - 1):
        if matrix[i][:-1] != matrix[i + 1][1:]:
            return False
    return True


def main():
    matrix = [[1, 2, 3, 4],
              [5, 1, 2, 3],
              [9, 5, 1, 2]]
    print(isToeplitzMatrix(matrix))


if __name__ == '__main__':
    main()