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
        if not head:
            return head
        dummy = head
        address = {}
        while dummy:
            if dummy in address:
                dummy = dummy.next
                continue
            else:
                newNode = Node(dummy.val)
                address[dummy] = newNode
                if dummy.random == None:
                    dummy = dummy.next
                    continue
                elif dummy.random in address:
                    newNode.random = address[dummy.random]
                else:
                    randNewNode = Node(dummy.random.val)
                    address[dummy.random] = randNewNode

            dummy = dummy.next
                
        dummy = head
        while dummy:
            address[dummy].next = address[dummy.next] if dummy.next else None
            address[dummy].random = address[dummy.random] if dummy.random else None
            dummy = dummy.next
        return address[head]