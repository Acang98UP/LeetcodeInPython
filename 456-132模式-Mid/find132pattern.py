from typing import List


def find132pattern(nums: List[int]) -> bool:
    N = len(nums)
    leftMin = [float("inf")] * N
    # print(leftMin)
    for i in range(1, N):
        leftMin[i] = min(leftMin[i - 1], nums[i - 1])
    stack = []
    for j in range(N - 1, -1, -1):
        numsk = float("-inf")
        while stack and stack[-1] < nums[j]:
            numsk = stack.pop()
        if leftMin[j] < numsk:
            return True
        stack.append(nums[j])
    return False


def main():
    # nums = [1, 2, 3, 4]
    nums = [1, 0, 1, -4, -3]
    print(find132pattern(nums))


if __name__ == '__main__':
    main()