from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[x] = y
            self.count -= 1


def numSimilarGroups(strs: List[str]) -> int:
    n, m = len(strs), len(strs[0])
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            count = 0
            for k in range(m):
                if strs[i][k] != strs[j][k]:
                    count += 1
                    if count > 2:
                        break
            if count in {0, 2}:
                uf.union(i, j)
    return uf.count


def main():
    strs = ["tars", "rats", "arts", "star"]
    print(numSimilarGroups(strs))


if __name__ == '__main__':
    main()