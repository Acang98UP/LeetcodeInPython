from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # solution 1: for loop
    i, temp = 0, 0
    maxLength = [0]
    while i < len(nums):
        if nums[i] == 1:
            temp += 1
        else:
            maxLength.append(temp)
            temp = 0
        i += 1
    return max(max(maxLength), temp)


def main():
    # nums = [1, 1, 1, 1, 0, 1, 1, 1]
    nums = [1]
    print(findMaxConsecutiveOnes(nums))


if __name__ == '__main__':
    main()