# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr, firstP, secondP = head, dummy, dummy
        while curr:
            newNode = ListNode(curr.val)
            if curr.val < x:
                newNode.next = firstP.next
                firstP.next = newNode
                firstP = newNode

            else:
                if secondP == dummy:
                    firstP.next = newNode
                    secondP = newNode
                else:
                    secondP.next = newNode
                    secondP = newNode
            curr = curr.next
        return dummy.next
