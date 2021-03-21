from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    row = []
    column = []
    for i in range(len(matrix)):
        if matrix[i].count(0) > 0:
            row.append(i)
    for j in range(len(matrix[0])):
        for i in range(len(row)):
            if matrix[row[i]][j] == 0:
                column.append(j)
    if column and row:
        for i in range(len(matrix[0])):
            for j in range(len(row)):
                matrix[row[j]][i] = 0
        for i in range(len(column)):
            for j in range(len(matrix)):
                matrix[j][column[i]] = 0




def main():
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[1,2,3,4],
              [5,0,7,8],
              [0,10,11,12],
              [13,14,15,0]]
    setZeros(matrix)
    print(matrix)


if __name__ == '__main__':
    main()