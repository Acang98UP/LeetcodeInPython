import collections
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    nums_set = collections.Counter(nums)
    # print(nums_set)
    res = []
    for i in range(1, len(nums) + 1):
        if i in nums_set:
            continue
        else:
            res.append(i)
    return res


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))


if __name__ == '__main__':
    main()