from typing import List


def regionsBySlashes(grid: List[str]) -> int:
    m, n = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(3 * n)] for _ in range(3 * m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '/':
                new_grid[3 * i][3 * j + 2] = 1
                new_grid[3 * i + 1][3 * j + 1] = 1
                new_grid[3 * i + 2][3 * j] = 1
            if grid[i][j] == '\\':
                new_grid[3 * i][3 * j] = 1
                new_grid[3 * i + 1][3 * j + 1] = 1
                new_grid[3 * i + 2][3 * j + 2] = 1

    def dfs(i, j):
        if 0 <= i < 3 * m and 0 <= j < 3 * n and new_grid[i][j] == 0:
            new_grid[i][j] = 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

    for i in range(3 * m):
        for j in range(3 * n):
            if new_grid[i][j] == 0:
                ans += 1
                dfs(i, j)
    return ans


def main():
    grid = [
      " /",
      "/ "
    ]

    print(regionsBySlashes(grid))


if __name__ == '__main__':
    main()