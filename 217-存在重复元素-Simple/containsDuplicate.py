from typing import List

# 利用set集合的特性：不能出现重复元素
# 直接判断是否有重复元素！！

def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    else:
        return True

    # 究极简化版
    # return len(set(nums)) != len(nums)

def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = containsDuplicate(nums)
    print(result)

if __name__ == '__main__':
    main()