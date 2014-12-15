class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        if not root:
            return []
        else:
            if root.left:
                result.extend(self.postorderTraversal(root.left))
            if root.right:
                result.extend(self.postorderTraversal(root.right))
            result.append(root.val)
        return result


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    root.right = b
    b.left = c
    print solution.postorderTraversal(root)
