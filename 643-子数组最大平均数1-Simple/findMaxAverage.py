from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    cur = sum(nums[:k])
    res = cur / k
    for i in range(k, len(nums)):
        cur = cur - nums[i - k] + nums[i]
        res = max(res, cur / k)
    return res


def main():
    # nums = [1, 12, -5, -6, 50, 3]
    # nums = [5]
    nums = [0, 1, 1, 3, 3]
    k = 4
    print(findMaxAverage(nums, k))


if __name__ == '__main__':
    main()