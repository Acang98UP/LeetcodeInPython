from typing import List


def countBits(num: int) -> List[int]:
    res = []
    for i in range(num + 1):
        res.append(bin(i).count('1'))
    return res


def main():
    num = 2
    print(countBits(num))


if __name__ == '__main__':
    main()