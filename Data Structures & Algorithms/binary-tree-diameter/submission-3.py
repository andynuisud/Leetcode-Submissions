# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #We can go through every node and have two global variables 
    #Then add them + 1 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0 

        def dfs(current):
            if not current: 
                return 0

            left = dfs(current.left)
            right = dfs(current.right)

            self.res = max(self.res, left + right)
            
            return 1 + max(left, right)
        dfs(root)
        return self.res