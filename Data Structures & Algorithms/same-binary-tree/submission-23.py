class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2): 

            if not node1 and not node2: 
                return True 
            
            if not node1 or not node2: 
                return False

            if node1.val != node2.val: 
                return False

            nodeLeft = dfs(node1.left, node2.left)
            nodeRight = dfs(node1.right, node2.right)

            return nodeLeft and nodeRight 

        return dfs(p, q)