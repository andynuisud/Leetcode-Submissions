# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        temp = []

        if not root: 
            return temp

        q = deque([root])

        while q: 
            level = []

            for _ in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)

                if curr.left: 
                    q.append(curr.left)

                if curr.right: 
                    q.append(curr.right)

            temp.append(level)

        res = []

        for i in temp: 
            res.append(i[-1])

        return res