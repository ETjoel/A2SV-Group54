# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        head.next = None
        while temp:
            temp2 = temp.next
            temp.next = head
            head = temp
            temp = temp2
        return head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr, leftHead = head, ListNode(float('inf'),head)
        counter = 1
        while curr and curr.next and counter != right:
            if counter+1 == left:
                leftHead = curr
            counter+=1
            curr = curr.next
        if leftHead and leftHead.next:
            print(leftHead.val, leftHead.next.val, curr.val)
            temp = leftHead.next
            tail = curr.next
            curr.next = None
            leftHead.next = self.reverseList(temp)
            temp.next = tail
            if leftHead.val == float('inf'):
                return leftHead.next
        return head