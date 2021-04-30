import collections
from typing import List


def singleNumber(nums: List[int]) -> int:
    counter = collections.Counter(nums)
    return counter.most_common(len(counter))[-1][0]


def main():
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(singleNumber(nums))


if __name__ == '__main__':
    main()