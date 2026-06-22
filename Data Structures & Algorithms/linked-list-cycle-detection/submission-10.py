# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        """
            Start slow and fast at the head 
            Iterate slow by 1 iterate fast by 2 

            while fast and fast.next

            If they move to the same node there is a cycle return true
            Else return false 
        """

        slow = head
        fast = head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast: 
                return True #There is a cycle

        return False

