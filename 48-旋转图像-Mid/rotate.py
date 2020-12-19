from typing import List


def rotate(matrix: List[List[int]]) -> List[List[int]]:
    length = len(matrix)
    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # 首先进行对角线变换
    for i in range(length):
        for j in range(length // 2):
            # 进行垂直对称轴变换
            matrix[i][j], matrix[i][length - j - 1] = matrix[i][length - j - 1], matrix[i][j]
    return matrix

def main():
    matrix = [
        [5, 11, 9, 11],
        [2, 4, 8, 10],
        [15, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    matrix = rotate(matrix)
    print(matrix)

if __name__ == '__main__':
    main()