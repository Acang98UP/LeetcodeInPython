from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, len(cost)):
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
    return min(dp[-2], dp[-1])

def main():
    cost = [10, 15, 20]
    print(minCostClimbingStairs(cost))

if __name__ == '__main__':
    main()