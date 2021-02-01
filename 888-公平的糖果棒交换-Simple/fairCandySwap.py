import collections
from typing import List


def fairCandySwap(A: List[int], B: List[int]) -> List[int]:
    diff = sum(B) - sum(A)
    dic = collections.Counter(A)
    print(dic)
    for b in B:
        if b - diff // 2 in dic:
            return [b - diff // 2, b]


def main():
    A = [1, 2, 5]
    B = [2, 4]
    print(fairCandySwap(A, B))


if __name__ == '__main__':
    main()