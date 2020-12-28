from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    if n <= 1:
        return 0
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    else:
        cost = [float('inf') for i in range(k + 1)]
        profit = [0 for i in range(k + 1)]
        for p in prices:
            for i in range(1, k + 1):
                cost[i] = min(cost[i], p - profit[i - 1])
                profit[i] = max(profit[i], p - cost[i])
        return profit[-1]



def main():
    k = 2
    prices = [2, 4, 1]
    print(maxProfit(k, prices))


if __name__ == '__main__':
    main()