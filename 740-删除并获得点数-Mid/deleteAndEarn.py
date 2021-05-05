import collections
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    maxNum = max(nums)
    num_sum = [0 for _ in range(maxNum + 1)]
    for x in nums:
        num_sum[x] += x

    a = num_sum[0]
    b = max(num_sum[0], num_sum[1])
    for x in range(2, maxNum + 1):
        old_b = b
        b = max(a + num_sum[x], b)
        a = old_b

    return b


def main():
    nums = [2, 2, 3, 3, 3, 4]
    print(deleteAndEarn(nums))


if __name__ == '__main__':
    main()