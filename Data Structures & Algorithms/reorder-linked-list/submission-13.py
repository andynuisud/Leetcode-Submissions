# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        """
            Use fast and slow pointers to check for the middle of the linked kist 
            Reverse the last part, then recompile a new linked list alternating the two sperate linkedlists 
        """

        fast = head
        slow = head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next

        previous = None
        current = slow.next
        slow.next = None

        while current: 
            temp = current.next
            current.next = previous 
            previous = current
            current = temp

        #Previous is the reversed second portion 

        first = head
        second = previous 

        while first and second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1 
            first, second = temp1, temp2 