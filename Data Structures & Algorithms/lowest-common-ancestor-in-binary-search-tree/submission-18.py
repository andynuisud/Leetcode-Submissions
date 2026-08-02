# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        """
            - If both P AND Q are smaller than the current node, the lowest common ancestor should be to 
            the left.
            - If both P AND Q are larger than the current node, the LCA should be to the right  
            - If P is less and Q is larger than the current node, the current node should be the LCA 

            Iteratively solve this. Keep traversing (curr = node) -> Keep checking until curr exists...
            Then check the previously stated conditions. If P < node.val < Q, return curr 
        """

        curr = root 

        while curr: 
            if p.val < curr.val and q.val < curr.val: 
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val: 
                curr = curr.right
            else: 
                return curr 
        