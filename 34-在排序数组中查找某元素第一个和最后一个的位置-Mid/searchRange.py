from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    begin, end = 0, -1
    if not nums:
        return [-1, -1]
    while begin < len(nums):
        if nums[begin] == target:
            temp = begin
            end = temp
            break
        begin += 1
    if begin == len(nums):
        return [-1, -1]
    while temp < len(nums):
        if nums[temp] == target:
            end = temp
        temp += 1
    return [begin, end]


def main():
    # nums = [5, 7, 7, 8, 8, 10]
    nums = [1]
    target = 1
    print(searchRange(nums, target))


if __name__ == '__main__':
    main()