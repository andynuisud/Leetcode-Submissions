# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
   
        """
            We want to find the middle of the list 
            After we find the middle of the list we just reverse
            Then we alternatively concatenate the lists together            
        """

        slow = head
        fast = head.next 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        #After this we want to get the middle 
        current = slow.next
        slow.next = None
        previous = None

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
            