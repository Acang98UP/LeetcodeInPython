from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res = []
    current = [root]
    sign = False
    while current:
        current_res = []
        next_node_list = []
        for node in current:
            if node:
                current_res.append(node.val)
                next_node_list.extend([node.left, node.right])
        if current_res:
            if sign:
                current_res = current_res[::-1]
            res.append(current_res)
        current = next_node_list
        sign = False if sign else True
    return res


def main(null=None):
    tree = [3, 9, 20, null, null, 15, 7]
    print(zigzagLevelOrder(tree))

if __name__ == '__main__':
    main()
