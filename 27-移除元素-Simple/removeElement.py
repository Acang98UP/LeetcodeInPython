from typing import List


def removeElement(nums: List[int], val: int) -> int:
    index = 0
    while index != len(nums):
        if nums[index] == val:
            nums.pop(index)
            continue
        else:
            index += 1
    return len(nums)


def main():
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement(nums, val))


if __name__ == '__main__':
    main()