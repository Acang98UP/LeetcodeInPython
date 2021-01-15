from typing import List


class UF:

    def __init__(self, M):
        self.parent = {}
        self.cnt = 0

    def find(self, x):
        if x not in self.parent:
            self.cnt += 1
            self.parent[x] = x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, p, q):
        if self.connected(p, q): return
        leader_p = self.find(p)
        leader_q = self.find(q)
        self.parent[leader_p] = leader_q
        self.cnt -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)


def removeStones(stones: List[List[int]]) -> int:
    n = len(stones)
    uf = UF(0)
    for i in range(n):
        uf.union(stones[i][0] + 10001, stones[i][1])
    return n - uf.cnt


def main():
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(removeStones(stones))


if __name__ == '__main__':
    main()