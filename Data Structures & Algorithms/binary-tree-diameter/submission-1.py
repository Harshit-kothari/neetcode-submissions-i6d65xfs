# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Just call the external helper
        return compute_diameter(root)


# 🔹 Function outside the class
def compute_diameter(root: Optional[TreeNode]) -> int:
    max_diameter = [0]   # use list to mutate inside dfs
    
    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        # update diameter at this node
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        
        # return height of this subtree
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return max_diameter[0]