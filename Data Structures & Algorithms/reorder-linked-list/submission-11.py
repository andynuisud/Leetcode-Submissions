# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
   
        """
            We iterate through the linked list and want to find the middle
            after finding the middle we want to split it in half 
            after splitting in haf we want to reverse the list
            after that we alternatively concatenate the rest 
        """

        dummy = head

        left = dummy
        right = dummy

        while right and right.next: 
            left = left.next
            right = right.next.next

        #now we want to split it in half 
        
        previous = None
        current = left.next
        left.next = None

        while current: 
            temp = current.next
            current.next = previous 
            previous = current
            current = temp

        first, second = head, previous 

        while first and second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2 
