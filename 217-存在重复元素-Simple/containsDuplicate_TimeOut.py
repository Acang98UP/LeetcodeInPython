from typing import List

# 会出现超时！！！

def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) == 0:
        return False
    else:
        new_List = []
        new_List.append(nums[0])
    # print(new_List)
    for i in range(1, len(nums)):
        try:
            new_List.remove(nums[i])
            return True
        except ValueError:
            new_List.append(nums[i])
    if len(new_List) == len(nums):
        return False

def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = containsDuplicate(nums)
    print(result)

if __name__ == '__main__':
    main()