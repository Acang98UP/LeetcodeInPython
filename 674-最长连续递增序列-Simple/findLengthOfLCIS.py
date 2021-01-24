from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1
    start, maxlength = 0, 0
    maxlist = [nums[start]]
    for end in range(1, len(nums)):
        if nums[end] > nums[end - 1]:
            maxlist.append(nums[end])
        else:
            if len(maxlist) > maxlength:
                maxlength = len(maxlist)
                maxlist.clear()
            start = end
            maxlist = [nums[start]]
    # print(maxlength)
    return max(maxlength, len(maxlist))


def main():
    nums = [1, 3, 5, 4, 2, 3, 4, 5]
    print(findLengthOfLCIS(nums))


if __name__ == '__main__':
    main()
