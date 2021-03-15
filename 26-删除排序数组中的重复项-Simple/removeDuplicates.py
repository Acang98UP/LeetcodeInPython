from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return len(nums)
    i = 0
    while i < len(nums) - 1:
        if nums[i] in nums[i + 1:]:
            nums.remove(nums[i])
            continue
        i += 1
    print(nums)
    return len(nums)


def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))


if __name__ == '__main__':
    main()