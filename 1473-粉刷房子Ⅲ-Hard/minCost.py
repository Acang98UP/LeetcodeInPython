from functools import lru_cache
from typing import List


def minCost(houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    @lru_cache(None)
    def dfs(idx, color, t):
        if t < 0 or t > m - idx:
            return float("inf")
        if idx == m:
            return 0
        curr = float("inf")
        if houses[idx]:
            if idx:
                if houses[idx] != houses[idx - 1]:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t))
            else:
                curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
        else:
            for i in range(1, n + 1):
                houses[idx] = i
                if idx > 0:
                    if i != houses[idx - 1]:
                        curr = min(curr, dfs(idx + 1, houses[idx], t - 1) + cost[idx][i - 1])
                    else:
                        curr = min(curr, dfs(idx + 1, houses[idx], t) + cost[idx][i - 1])
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1) + cost[idx][i - 1])
            houses[idx] = 0
        return curr

    res = dfs(0, 0, target)
    if res == float("inf"):
        return -1
    return res


def main():
    houses = [0, 0, 0, 0, 0]
    cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m = 5
    n = 2
    target = 3
    print(minCost(houses, cost, m, n, target))


if __name__ == '__main__':
    main()