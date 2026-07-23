# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #use a DFS for this problem 

        self.boolean = True
        
        def dfs(node):
            if not node: return 0

            leftNum = dfs(node.left)
            rightNum = dfs(node.right)

            if abs(leftNum - rightNum) > 1: self.boolean = False

            return 1 + max(leftNum, rightNum)

        dfs(root)
        return self.boolean