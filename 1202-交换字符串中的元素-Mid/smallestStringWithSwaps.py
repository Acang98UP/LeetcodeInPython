import collections
from typing import List


def smallestStringWithSwaps(s: str, pairs: List[List[int]]) -> str:
    # 建图
    graph = [[] for _ in range(len(s))]
    visited = [0] * len(s)
    for x, y in pairs:
        graph[x].append(y)
        graph[y].append(x)

    res = list(s)
    for i in range(len(s)):
        if not visited[i]:
            # 获取联通节点
            connected_nodes = []
            bfs(connected_nodes, graph, visited, i)
            # 重新赋值
            indices = sorted(connected_nodes)
            string = sorted(res[node] for node in connected_nodes)
            for j, ch in zip(indices, string):
                res[j] = ch

    return "".join(res)

def bfs(res, graph, visited, x):
    queue = collections.deque([x])
    visited[x] = 1
    res.append(x)

    while queue:
        cur_node = queue.popleft()
        for neighbor in graph[cur_node]:
            if visited[neighbor]:
                continue
            visited[neighbor] = 1
            res.append(neighbor)
            queue.append(neighbor)


def main():
    s = 'dcab'
    pairs = [[0, 3], [1, 2]]
    print(smallestStringWithSwaps(s, pairs))


if __name__ == '__main__':
    main()