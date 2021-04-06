from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)
    else:
        index = 1
        flag = 0
        while index != len(nums):
            if nums[index] == nums[index - 1] and flag == 0:
                index += 1
                flag = 1
            elif nums[index] == nums[index - 1] and flag == 1:
                # 该情况是已经有了两个相同的，这个是需要去除的
                nums.pop(index)
            elif nums[index] != nums[index - 1]:
                index += 1
                flag = 0
    return len(nums)




def main():
    nums = [1, 1, 1, 2, 2, 3]
    print(removeDuplicates(nums))


if __name__ == '__main__':
    main()