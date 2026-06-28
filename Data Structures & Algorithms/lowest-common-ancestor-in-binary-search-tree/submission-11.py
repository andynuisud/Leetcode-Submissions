# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        self.lowest = root

        def dfs(node): 

            if not node: 
                return None

            if p.val > node.val and q.val > node.val: 
                dfs(node.right) 
            elif p.val < node.val and q.val < node.val: 
                dfs(node.left)
            else: 
                self.lowest = node

        dfs(root)

        return self.lowest