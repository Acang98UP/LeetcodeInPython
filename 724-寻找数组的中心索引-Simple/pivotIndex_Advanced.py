from typing import List


def pivotIndex(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return -1
    sum_all = sum(nums)
    sum1 = 0
    for i in range(len(nums)):
        sum1 += nums[i]
        if sum1 - nums[i] == sum_all - sum1:
            return i
    return -1


def main():
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    nums = [-1, -1, -1, 1, 1, 1]
    print(pivotIndex(nums))


if __name__ == '__main__':
    main()