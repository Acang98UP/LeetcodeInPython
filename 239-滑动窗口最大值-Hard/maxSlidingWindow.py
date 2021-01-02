from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    begin, end = 0, 0 + k
    while end <= (len(nums)):
        temp = nums[begin:end]
        res2 = max(temp)
        res.append(res2)
        begin += 1
        end += 1
    return res


def main():
    nums = [1, -1]
    k = 1
    print(maxSlidingWindow(nums, k))


if __name__ == '__main__':
    main()