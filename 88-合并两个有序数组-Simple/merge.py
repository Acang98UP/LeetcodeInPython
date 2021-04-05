from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # l为nums1的m开始索引, r为nums2的n开始索引，index为修改nums1的开始索引，然后从nums1末尾开始往前遍历
    l, r, index = m - 1, n - 1, len(nums1) - 1
    # 按从大到小，从后往前修改nums1的值，每次都赋值为nums1和nums2的当前索引的较大值，然后移动索引
    while l >= 0 and r >= 0:
        # 如果nums1[l] >= nums2[r]，则先赋值为nums1[l]，l索引减少
        if nums1[l] >= nums2[r]:
            nums1[index] = nums1[l]
            l -= 1
        else:
            # 如果nums1[l] <= nums2[r]，则先赋值为nums2[r]，r索引减少
            nums1[index] = nums2[r]
            r -= 1
        # 当前nums1修改索引减少1
        index -= 1
    # nums2没有遍历完n个，则继续遍历，直到n个完成
    while r >= 0:
        nums1[index] = nums2[r]
        r -= 1
        index -= 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, m, nums2, n))


if __name__ == '__main__':
    main()