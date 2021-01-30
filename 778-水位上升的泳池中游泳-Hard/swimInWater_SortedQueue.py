from typing import List
import bisect


def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    b = {(0, 0)}  # 访问标记
    p = [[grid[0][0], 0, 0]]  # 升序队列初始化
    t = 0  # 途径最大时间标记
    while True:
        h, i, j = p.pop(0)
        t = max(t, h)
        if i == j == n - 1:  # 找到终点就就返回时间
            return t
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= x < n and 0 <= y < n and (x, y) not in b:
                bisect.insort(p, [grid[x][y], x, y])  # 二分插入
                b |= {(x, y)}



def main():
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swimInWater(grid))


if __name__ == '__main__':
    main()