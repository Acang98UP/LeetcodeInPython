import collections
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    deque = collections.deque()
    res = []
    for i, num in enumerate(nums):
        if deque and deque[0] <= i - k:
            deque.popleft()
        while deque and num > nums[deque[-1]]:
            deque.pop()
        deque.append(i)
        if i >= k - 1:
            res.append(nums[deque[0]])
    return res


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(maxSlidingWindow(nums, k))


if __name__ == '__main__':
    main()