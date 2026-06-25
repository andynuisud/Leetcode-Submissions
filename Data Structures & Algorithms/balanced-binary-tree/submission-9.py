# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #We want to get the height of both sides 
        #Subtract both, and if greater than 1, return False else return True 

        #dfs(current.left)

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == -1 or right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
        
        return dfs(root) != -1