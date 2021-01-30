from typing import List
import bisect


def swimInWater(grid: List[List[int]]) -> int:
    n = len(grid)
    b, e = {(0, 0)}, {(n - 1, n - 1)}  # 双向访问标记
    p, q = [[grid[0][0], 0, 0]], [[grid[-1][-1], n - 1, n - 1]]  # 双向升序队列初始化
    t = 0  # 途径最大时间标记
    while True:
        h, i, j = p.pop(0)
        t = max(t, h)
        if (i, j) in e:  # 如果找到的点已经存在于另一个队列里，就返回答案
            return t
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= x < n and 0 <= y < n and (x, y) not in b:
                bisect.insort(p, [grid[x][y], x, y])
                b |= {(x, y)}

        h, i, j = q.pop(0)  # 从这里开始都是对称的，调换p，q，b，e就行。
        t = max(t, h)
        if (i, j) in b:
            return t
        for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= x < n and 0 <= y < n and (x, y) not in e:
                bisect.insort(q, [grid[x][y], x, y])
                e |= {(x, y)}



def main():
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    print(swimInWater(grid))


if __name__ == '__main__':
    main()