from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) // 2 == 0:
        pass
    return 0

def main():
    nums = [1, 2, 3, 1]
    print(rob(nums))


if __name__ == '__main__':
    main()