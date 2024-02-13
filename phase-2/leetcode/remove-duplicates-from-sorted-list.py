# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        filtered = head
        curr = head.next
        while curr:
            if filtered.val != curr.val:
                filtered.next = curr
                filtered = curr
            curr = curr.next
        filtered.next = None
        return head

