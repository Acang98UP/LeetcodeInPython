from typing import List


def getRow(rowIndex: int) -> List[int]:
    res = [1]
    for i in range(1, rowIndex + 1):
        res.append(int(res[i - 1] * (rowIndex - i + 1) / i))
    return res


def main():
    rowIndex = 13
    print(getRow(rowIndex))


if __name__ == '__main__':
    main()