# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """
            -Use a tail node find the end 
            -After we find the end and find the index in which how far
            its from the tail node 
            -Iterate through the front and append to a new listnode
            -Skip over it in that specific index 
        """ 

        current = tail = head

        index = 0

        while current: 
            current = current.next 
            tail = tail.next
            index += 1

        dummy = ListNode(0)
        dummy.next = head
        current = dummy 

        i = 0 

        while current: 
            if i == index - n: 
                current.next = current.next.next
            else:
                current = current.next

            i+= 1
        
        return dummy.next

