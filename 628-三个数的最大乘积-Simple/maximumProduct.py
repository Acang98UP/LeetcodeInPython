from typing import List


def maximumProduct(nums: List[int]) -> int:
    nums = sorted(nums)
    if nums[0] < 0 and nums[1] < 0:
        maxNumber = max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
    else:
        maxNumber = nums[-1] * nums[-2] * nums[-3]
    return maxNumber


def main():
    nums = [-100,-98,-1,2,3,4]
    print(maximumProduct(nums))


if __name__ == '__main__':
    main()