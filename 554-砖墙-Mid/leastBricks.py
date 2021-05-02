import collections
from typing import List


def leastBricks(wall: List[List[int]]) -> int:
    n, hm = len(wall), collections.Counter()
    print(hm)
    for w in wall:
        pre, index = 0, 0
        while index < len(w):
            hm[w[index] + pre] += 1
            pre, index = pre + w[index], index + 1
        del hm[pre]
    res = n
    for value in hm.values():
        res = min(res, n - value)
    return res


def main():
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(leastBricks(wall))


if __name__ == '__main__':
    main()