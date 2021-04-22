import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        Row, Col = len(matrix), len(matrix[0])
        res = float('-inf')
        for L in range(Col):  # L为左边界
            row_sum = [0 for _ in range(Row)]  # L为左边界R为右边界，各行的和
            for R in range(L, Col):
                for r in range(Row):
                    row_sum[r] += matrix[r][R]

                presum = [0]  # 前缀和
                cur_sum = 0  # 当前的前缀和
                for rowsum in row_sum:
                    cur_sum += rowsum
                    idx = bisect.bisect_left(presum, cur_sum - k)  # 第一个大于等于cur_sum - k的值的index
                    if idx < len(presum):
                        res = max(res, cur_sum - presum[idx])
                    bisect.insort(presum, cur_sum)
        return res