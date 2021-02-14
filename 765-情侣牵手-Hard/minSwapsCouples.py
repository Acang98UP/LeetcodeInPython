from typing import List


def minSwapsCouples(row: List[int]) -> int:
    N = len(row)
    res = 0
    for i in range(0, N - 1, 2):
        if row[i] == row[i + 1] ^ 1:
            continue
        for j in range(i + 1, N):
            if row[i] == row[j] ^ 1:
                row[i + 1], row[j] = row[j], row[i + 1]
        res += 1
    return res


def main():
    row = [0, 2, 1, 3]
    print(minSwapsCouples(row))


if __name__ == '__main__':
    main()