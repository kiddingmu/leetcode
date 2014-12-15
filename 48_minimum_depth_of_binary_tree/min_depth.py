class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # return an integer
    def minDepth(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            left_mark = False
            right_mark = False
            if root.left:
                min_left = 1 + self.minDepth(root.left)
                left_mark = True
            if root.right:
                min_right = 1 + self.minDepth(root.right)
                right_mark = True
            if left_mark and right_mark:
                return min(min_left, min_right)
            elif left_mark:
                return min_left
            elif right_mark:
                return min_right

if __name__ == "__main__":
    solution = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    A.left = B
    print solution.minDepth(A)
