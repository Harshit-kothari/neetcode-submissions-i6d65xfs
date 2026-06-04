# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if not root:
        return 0
    return (1 + max(height(root.left),height(root.right)))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # diameter through the root
        left_height = height(root.left)
        right_height = height(root.right)
        root_diameter = left_height + right_height
        
        # diameter in left and right subtrees
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        # max of all three
        return max(root_diameter, left_diameter, right_diameter)
        