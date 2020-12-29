from typing import List


def minPatches(nums: List[int], n: int) -> int:
    add, i, count = 1, 0, 0
    while add <= n:
        if i < len(nums) and nums[i] <= add:
            add += nums[i]  # from [1, add] to [1, add + nums[i]]
            i += 1
        else:
            add += add  # from [1, add] to [1, 2add]
            count += 1
    return count


def main():
    nums = [1, 2]
    n = 6
    print(minPatches(nums, n))


if __name__ == '__main__':
    main()