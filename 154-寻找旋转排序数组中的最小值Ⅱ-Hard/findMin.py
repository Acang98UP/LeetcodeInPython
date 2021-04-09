from typing import List


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        # mid = left + (right - left) // 2
        mid = (left + right) >> 1
        if nums[mid] > nums[right]:
            # mid 肯定不是最小值
            # [7,8,9,10,11,1,2,3]
            left = mid + 1
        elif nums[mid] < nums[right]:
            # mid 有可能是最小值
            # [7,8,1,2,3]
            right = mid
        else:
            # 都有可能，所以就把 right 排除了
            # [1,1,1,1,1,0,1]
            assert nums[mid] == nums[right]
            right = right - 1
    # 无需后处理
    return nums[left]


def main():
    nums = [1, 3, 5]
    print(findMin(nums))


if __name__ == '__main__':
    main()