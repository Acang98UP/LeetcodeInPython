from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        # nums[l] <= nums[r]说明当前只有一个元素或者没有旋转，直接返回nums[l]即是最小值
        if nums[l] <= nums[r]:
            return nums[l]
        else:
            mid = (l + r) >> 1
            # 左边有序,最小值在右边,这里有=号是为了处理[2,1]这种情况
            if nums[l] <= nums[mid]:
                l = mid + 1
            # 右边有序，最小值应该有可能在左边，注意：应该包括nums[mid]，因为该最小值有可能就是nums[mid]
            elif nums[r] > nums[mid]:
                r = mid


def main():
    nums = [3, 4, 5, 1, 2]
    print(findMin(nums))


if __name__ == '__main__':
    main()