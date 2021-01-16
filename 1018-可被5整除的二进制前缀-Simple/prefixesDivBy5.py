from typing import List


def prefixesDivBy5(A: List[int]) -> List[bool]:
    res = []
    pre = 0
    for i in A:
        pre = ((pre << 1) + i) % 5
        res.append(not pre)
    return  res


def main():
    A = [0, 1, 1]
    print(prefixesDivBy5(A))


if __name__ == '__main__':
    main()
