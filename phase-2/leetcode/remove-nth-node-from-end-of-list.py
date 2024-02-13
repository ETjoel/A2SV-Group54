# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
    
        while fast.next:
            if n <= 0:
                slow = slow.next
            fast = fast.next
            n-=1
        if slow.next:
            slow.next = slow.next.next
        return dummy.next

