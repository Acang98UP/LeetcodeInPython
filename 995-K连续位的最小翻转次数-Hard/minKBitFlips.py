import collections
from typing import List


def minKBitFlips(nums: List[int], K: int) -> int:
    N = len(nums)
    que = collections.deque()
    res = 0
    for i in range(N):
        if que and i >= que[0] + K:
            que.popleft()
        if len(que) % 2 == nums[i]:
            if i + K > N:
                return -1
            que.append(i)
            res += 1
    return res


def main():
    nums = [1, 1, 0]
    K = 2
    print(minKBitFlips(nums, K))


if __name__ == '__main__':
    main()