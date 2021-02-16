from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[::2])


def main():
    nums = [1, 4, 2, 3]
    print(arrayPairSum(nums))


if __name__ == '__main__':
    main()