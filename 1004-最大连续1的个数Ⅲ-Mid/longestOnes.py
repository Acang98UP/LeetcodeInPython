from typing import List


def longestOnes(A: List[int], K: int) -> int:
    # 滑动窗口
    N = len(A)
    res = 0
    left, right = 0, 0
    zeros = 0
    while right < N:
        if A[right] == 0:
            zeros += 1
        while zeros > K:
            if A[left] == 0:
                zeros -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res


def main():
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    print(longestOnes(A, K))


if __name__ == '__main__':
    main()