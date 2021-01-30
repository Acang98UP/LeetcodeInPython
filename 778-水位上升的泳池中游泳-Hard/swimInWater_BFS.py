from typing import List
import sys, time


def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    c = {(0, 0)}  # 访问标记
    for t in range(max(grid[0][0], grid[-1][-1]), sys.maxsize):  # 从首末元素的最大时间作为最开始的判断条件
        p = c.copy()  # 宽搜队列初始化，每个时间点的初始状态是上一轮时间访问标记过的坐标
        while p:
            q = set()  # 下一批宽搜队列
            for i, j in p:
                if i == j == n - 1:  # 如果走到目标了就返回时间
                    return t
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] <= t and (x, y) not in c:  # 符合时空条件就扩散地图
                        q |= {(x, y)}
                        c |= {(x, y)}
            p = q


def main():
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swimInWater(grid))


if __name__ == '__main__':
    main()