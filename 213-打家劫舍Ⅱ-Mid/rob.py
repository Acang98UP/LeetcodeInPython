class Solution(object):
    def rob(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        return max(self.rob1(nums[0:N - 1]), self.rob1(nums[1:N]))

    def rob1(self, nums):
        N = len(nums)
        if not nums:
            return 0
        if N == 1:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]