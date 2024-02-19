# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        val, rem = n//k, n%k
        curr = head
        counter = 1
        res = [head]
        print(val, rem)
        while curr:
            print(counter, curr.val)
            if rem and counter == val+1:
                # print(curr.val)
                res.append(curr.next)
                temp = curr.next
                curr.next = None
                curr = temp
                counter = 1
                rem-=1
            elif not rem and counter == val :
                # print(curr.val)
                res.append(curr.next)
                temp = curr.next
                curr.next = None
                curr = temp
                counter = 1
            else: 
                counter+=1
                curr = curr.next
        for i in range(51):
            res.append(None)
        return res[:k]