from typing import List


def pivotIndex(nums: List[int]) -> int:
    if len(nums) == 0 or len(nums) == 1:
        return -1
    head_index, tail_index = 0, -1
    head_sum, tail_sum = 0, 0
    templen = len(nums)
    nums = [0] + nums + [0]
    # print(nums)
    for mid_point in range(len(nums)):
        while head_index < mid_point:
            head_sum += nums[head_index]
            head_index += 1
        while (tail_index + len(nums)) > mid_point:
            tail_sum += nums[tail_index]
            tail_index -= 1
        if head_sum == tail_sum and mid_point != 0:
            if mid_point > templen:
                return -1
            else:
                return mid_point - 1
        head_index, tail_index = 0, -1
        head_sum, tail_sum = 0, 0
    return -1



def main():
    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [1, 2, 3]
    nums = [-1, -1, -1, 1, 1, 1]
    print(pivotIndex(nums))


if __name__ == '__main__':
    main()