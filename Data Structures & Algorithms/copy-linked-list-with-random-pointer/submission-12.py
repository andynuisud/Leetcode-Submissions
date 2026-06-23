"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """
            - Have a first pass, iterate through the first node 
            and store it in a hashMap 
            - Then iterate through the hashmap, and link the random node
            to the actual one
        """

        hashMap = {}

        curr = head

        while curr: 
            hashMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr: 
            if curr.next: 
                hashMap[curr].next = hashMap[curr.next]
            if curr.random: 
                hashMap[curr].random = hashMap[curr.random]

            curr = curr.next

        if not head: 
            return None

        return hashMap[head]

