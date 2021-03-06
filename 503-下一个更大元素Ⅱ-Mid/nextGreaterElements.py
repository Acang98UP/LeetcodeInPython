from typing import List


def nextGreaterElements(nums: List[int]) -> List[int]:
    length = len(nums)
    res = [-1] * length
    stack = []
    for i in range(length * 2):
        while stack and nums[stack[-1]] < nums[i % length]:
            res[stack.pop()] = nums[i % length]
        stack.append(i % length)
    return res


def main():
    nums = [1, 2, 1]
    print(nextGreaterElements(nums))


if __name__ == '__main__':
    main()