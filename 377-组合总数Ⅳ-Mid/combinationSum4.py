from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    res = 0
    for i in range(target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]


def main():
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))


if __name__ == '__main__':
    main()