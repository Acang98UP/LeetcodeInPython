# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = self.bfs(root1)
        res2 = self.bfs(root2)
        return res1 == res2

    def bfs(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        a = []
        Q = [(0, root)]
        delta = 1000000000
        while Q:
            cur_len = len(Q)
            for _ in range(cur_len):
                ID, x = Q.pop(0)
                if x.left == None and x.right == None:
                    a.append((ID, x.val))
                if x.left:
                    left_ID = ID - delta
                    Q.append((left_ID, x.left))
                if x.right:
                    right_ID = ID + delta
                    Q.append((right_ID, x.right))
            delta //= 2

        a.sort(key = lambda x: x[0])
        res = []
        for ID, x in a:
            res.append(x)
        return res