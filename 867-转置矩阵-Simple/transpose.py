from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    row, column = len(matrix), len(matrix[0])
    res, temp = [], []
    for i in range(column):
        for j in range(row):
            temp.append(matrix[j][i])
        res.append(temp)
        temp = []
    return res


def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    # target = [[1, 4, 7],
    #           [2, 5, 8],
    #           [3, 6, 9]]
    print(transpose(matrix))


if __name__ == '__main__':
    main()