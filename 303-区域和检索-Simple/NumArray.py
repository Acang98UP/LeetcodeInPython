from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.preSum = [0] * (N + 1)
        for i in range(N):
            self.preSum[i + 1] = self.preSum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j + 1] - self.preSum[i]
