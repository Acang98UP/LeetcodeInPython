from typing import List


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    p = [[i] for i in range(len(edges) + 1)]  # 并查集初始化
    for x, y in edges:
        if p[x] is not p[y]:  # 如果两个集合地址不一样
            if len(p[x]) < len(p[y]):  # 权重优化判断
                x, y = y, x
            p[x].extend(p[y])  # 合并集合
            for z in p[y]:
                p[z] = p[x]  # 修改元素集合标记的指针地址
        else:
            return [x, y]


def main():
    edges = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantConnection(edges))


if __name__ == '__main__':
    main()