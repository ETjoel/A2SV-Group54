# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001, head)
        curr = dummy
        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                swapNode = ListNode(curr.next.val)
                curr.next = curr.next.next
                temp = dummy
                while temp and temp.next and temp != curr:
                    if swapNode.val <= temp.next.val:
                        swapNode.next = temp.next
                        temp.next = swapNode
                        break
                    temp = temp.next
        return dummy.next


        
