# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head 
        while curr:
            count +=1
            curr = curr.next
        if count == 1:
            return None
        if count == n:
            return head.next
        step = 0
        targetNode = head
        while step < count - n - 1:
            step  += 1
            targetNode = targetNode.next
        print(targetNode.val)
        targetNode.next = targetNode.next.next

        return head