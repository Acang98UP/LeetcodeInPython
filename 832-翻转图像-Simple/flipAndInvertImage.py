from typing import List


def flipAndInvertImage(A: List[List[int]]) -> List[List[int]]:
    for row in A:
        for j in range((len(row) + 1) // 2):
            if row[j] == row[-1 - j]:  # 采用Python化的符号索引
                row[j] = row[-1 - j] = 1 - row[j]
    return A


def main():
    A = [[1, 1, 0],
         [1, 0, 1],
         [0, 0, 0]]
    print(flipAndInvertImage(A))


if __name__ == '__main__':
    main()