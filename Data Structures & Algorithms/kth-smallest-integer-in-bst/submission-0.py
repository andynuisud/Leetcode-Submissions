# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
            Create an array: [1, 2, 3, 4, 5, 6]
            Get the Kth value from this array 
        """

        arr = []
        stack = []

        curr = root

        while curr or stack: 
            while curr: 
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            arr.append(curr.val)
            curr = curr.right

        for i in range(len(arr)):
            if i == k-1: 
                return arr[i]

        return -1 

