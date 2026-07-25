class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        i = 0 

        while current: 
            i += 1 
            current = current.next

        difference = i - n
        if difference == 0: 
            return head.next

        current = head

        for i in range(difference):
            if (i + 1) == difference:
                current.next = current.next.next
                break
            current = current.next

        return head   