# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return None

        tempLeft = root.left
        tempRight = root.right

        root.right = tempLeft
        root.left = tempRight

        self.invertTree(tempLeft)
        self.invertTree(tempRight)

        return root