# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
        Start iterating from n, then do fast and slow pointers from the end. 
        The slow pointer would be before the one that we want to skip
        """

        dummy = ListNode(0, head)
        
        fast = slow = dummy

        index = 0 

        while index < n: 
            fast = fast.next
            index += 1

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next

