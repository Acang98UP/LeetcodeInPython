from typing import List


def checkPossibility(nums: List[int]) -> bool:
    N = len(nums)
    count = 0
    for i in range(1, N):
        if nums[i] < nums[i - 1]:
            count += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return count <= 1


def main():
    nums = [3, 4, 2, 3]
    print(checkPossibility(nums))


if __name__ == '__main__':
    main()