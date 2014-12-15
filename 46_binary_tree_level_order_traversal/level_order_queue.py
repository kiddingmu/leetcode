#from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        queue = []
        if root:
            queue.append(root)
            level_result = []
            node_list = []
            while queue:
                curNode = queue[0]
                node_list.append(curNode)
                queue = queue[1:]
                if len(queue):
                    continue
                else:
                    for item in node_list:
                        level_result.append(item.val)
                        if item.left:
                            queue.append(item.left)
                        if item.right:
                            queue.append(item.right)
                    result.append(level_result)
                    level_result = []
                    node_list = []
            return result
        else:
            return []


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    G = TreeNode(7)
    H = TreeNode(8)
    root.left = B
    root.right = C
    B.left = D
    B.right = E
    C.left = F
    F.left = G
    F.right = H
    print solution.levelOrder(root)
