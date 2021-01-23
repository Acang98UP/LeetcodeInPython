from typing import List


class UnionFind:
    def __init__(self, size):
        self.father = [None] * size
        self.num_of_sets = size

    def find(self, x):
        """
        路径压缩
        """
        if self.father[x] is None:
            return x

        self.father[x] = self.find(self.father[x])

        return self.father[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        self.father[root_x] = root_y
        self.num_of_sets -= 1


def makeConnected(n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
        return -1

    uf = UnionFind(n)

    for n1, n2 in connections:
        if uf.is_connected(n1, n2):
            continue
        uf.merge(n1, n2)

    return uf.num_of_sets - 1


def main():
    n = 4
    connections = [[0, 1], [0, 2], [1, 2]]
    print(makeConnected(n, connections))


if __name__ == '__main__':
    main()
