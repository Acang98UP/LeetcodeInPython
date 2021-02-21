from typing import List
from sortedcontainers import SortedList


def longestSubarray(nums: List[int], limit: int) -> int:
    s = SortedList()
    left, right = 0, 0
    res = 0
    while right < len(nums):
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


def main():
    nums = [8, 2, 4, 7]
    limit = 4
    print(longestSubarray(nums, limit))


if __name__ == '__main__':
    main()