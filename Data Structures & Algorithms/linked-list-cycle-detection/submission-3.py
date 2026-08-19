# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head

        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
    
            if p1 == p2:
                return True
            if p1 is None:
                return False
        return False
            