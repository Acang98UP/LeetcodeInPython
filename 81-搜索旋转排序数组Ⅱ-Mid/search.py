from typing import List


def search(nums: List[int], target: int) -> bool:
    # 法1：直接判断, 复杂度O(n)
    # return target in nums
    # 法2：使用二分法, 复杂度O(logn)
    if not nums:
        return False
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        if nums[left] == nums[right]:
            left += 1
            continue
        if nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] > target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
    return False



def main():
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(search(nums, target))


if __name__ == '__main__':
    main()