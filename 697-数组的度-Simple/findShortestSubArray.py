import collections
from typing import List


def findShortestSubArray(nums: List[int]) -> int:
    left, right = dict(), dict()
    counter = collections.Counter(nums)
    for i, num in enumerate(nums):
        if num not in left:
            left[num] = i
        right[num] = i
        counter[num] += 1
    degree = max(counter.values())
    res = len(nums)
    for k, v in counter.items():
        if v == degree:
            res = min(res, right[k] - left[k] + 1)
    return res


def main():
    nums = [1, 2, 2, 3, 1]
    print(findShortestSubArray(nums))


if __name__ == '__main__':
    main()