class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = l1
        carry = 0

        while l1 or l2 or carry:        
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            total = v1 + v2 + carry 
            carry, val = divmod(total, 10) 

            # In-Place 
            if l1:
                l1.val = val
                curr = l1
                l1 = l1.next
            elif l2:
                curr.next = l2
                l2.val = val
                curr = l2
            else: # l1-> None, l2->None, carry = 1
                curr.next = ListNode(val)
                curr = curr.next
            
            if l2:
                l2 = l2.next

        return dummy.next

