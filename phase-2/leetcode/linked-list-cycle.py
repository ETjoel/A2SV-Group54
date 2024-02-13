# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rab, tor = head, head
        while tor and tor.next:
            tor = tor.next.next
            rab = rab.next
            if rab is tor: return True
        return False
        
