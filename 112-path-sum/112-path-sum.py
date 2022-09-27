# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        new_sum = targetSum - root.val
        if new_sum == 0 and root.left is None and root.right is None:
            return True
        if self.hasPathSum(root.left, new_sum): return True
        if self.hasPathSum(root.right, new_sum): return True
        return False  