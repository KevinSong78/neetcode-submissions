# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        # List is split now
        prev = None

        # This loop reverses the second half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # second is null, but prev is the new head of the reversed list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # because second needs to be inserted between first and first.next (which is tmp1)
            first, second = tmp1, tmp2