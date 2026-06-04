# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def height(root):
    if not root:
        return 0
    return (1+max(height(root.left), height(root.right)))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_height = 0
        right_height = 0
        left_height = max(left_height, height(root.left))
        right_height = max(right_height, height(root.right))

        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)